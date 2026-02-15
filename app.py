from flask import Flask, render_template, request, redirect, session, flash, Response, url_for
from models import db, User, Doctor, Appointment, ContactMessage
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import csv
import io
import random
import string

app = Flask(__name__)
app.secret_key = "secure_key_123"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# --- UTILITIES ---
def generate_meet_link():
    """Generates a random Google Meet-style link."""
    chars = string.ascii_lowercase
    part1 = ''.join(random.choices(chars, k=3))
    part2 = ''.join(random.choices(chars, k=4))
    part3 = ''.join(random.choices(chars, k=3))
    return f"https://meet.google.com/{part1}-{part2}-{part3}"

# --- INITIALIZATION ---
with app.app_context():
    db.create_all()
    # Create Default Admin
    if not User.query.filter_by(role='admin').first():
        admin = User(name="System Admin", email="admin@hospital.com", 
                     password=generate_password_hash("admin123"), role="admin")
        db.session.add(admin)
        
        # Create Default Doctors
        docs = [
            ("Dr. Sarah Jenkins", "Cardiology", 15),
            ("Dr. Mike Ross", "Neurology", 10),
            ("Dr. Emily Blunt", "Pediatrics", 8),
            ("Dr. John Doe", "Orthopedics", 12),
            ("Dr. Lisa Kudrow", "Dermatology", 20),
            ("Dr. Raj Malhotra", "General Physician", 18)  # ✅ ADD THIS
            ]

        for name, spec, exp in docs:
            if not Doctor.query.filter_by(name=name).first():
                db.session.add(Doctor(name=name, specialization=spec, experience=exp))
        db.session.commit()

# --- PUBLIC ROUTES ---
@app.route('/')
def index():
    doctors = Doctor.query.all()
    return render_template('index.html', doctors=doctors)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '').lower()
    if not query:
        return redirect('/')
    
    # Smart Symptom Mapping
    specialization = None
    if any(x in query for x in ["heart", "chest", "pulse", "cardio"]): specialization = "Cardiology"
    elif any(x in query for x in ["skin", "rash", "acne", "derma"]): specialization = "Dermatology"
    elif any(x in query for x in ["bone", "knee", "joint", "fracture"]): specialization = "Orthopedics"
    elif any(x in query for x in ["child", "baby", "infant", "kid"]): specialization = "Pediatrics"
    elif any(x in query for x in ["brain", "head", "nerve", "neuro"]): specialization = "Neurology"
    
    if specialization:
        doctors = Doctor.query.filter_by(specialization=specialization).all()
        flash(f"Showing specialists for '{query}'", "info")
    else:
        # Search by doctor name
        doctors = Doctor.query.filter(Doctor.name.ilike(f"%{query}%")).all()
        
    return render_template('index.html', doctors=doctors, search_query=query)

@app.route('/contact', methods=['POST'])
def contact():
    # Save the message to DB
    msg = ContactMessage(
        name=request.form['name'], 
        email=request.form['email'], 
        message=request.form['message']
    )
    db.session.add(msg)
    db.session.commit()
    
    # TRIGGERS THE GREEN ALERT BOX
    flash("Message sent successfully! We will contact you soon.", "success")
    return redirect('/#contact')

# --- AUTH ROUTES ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        if user and check_password_hash(user.password, request.form['password']):
            session['user_id'] = user.id
            session['role'] = user.role
            session['name'] = user.name
            return redirect('/admin' if user.role == 'admin' else '/dashboard')
        flash("Invalid credentials", "error")
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if User.query.filter_by(email=request.form['email']).first():
            flash("Email already exists", "error")
            return redirect('/register')
        user = User(
            name=request.form['name'],
            email=request.form['email'],
            password=generate_password_hash(request.form['password']),
            phone=request.form['phone']
        )
        db.session.add(user)
        db.session.commit()
        flash("Registration successful! Please login.", "success")
        return redirect('/login')
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

# --- PATIENT ROUTES ---
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session or session['role'] != 'patient': return redirect('/login')
    appointments = Appointment.query.filter_by(patient_id=session['user_id']).order_by(Appointment.date.desc()).all()
    return render_template('dashboard.html', appointments=appointments)

def assign_doctor(symptoms):
    if not symptoms:
        return None

    symptoms = symptoms.lower()

    # GENERAL PHYSICIAN CASES
    if any(x in symptoms for x in ["fever", "headache", "cold", "cough", "chest pain"]):
        specialization = "General Physician"

    elif any(x in symptoms for x in ["heart", "pulse"]):
        specialization = "Cardiology"

    elif any(x in symptoms for x in ["brain", "nerve"]):
        specialization = "Neurology"

    elif any(x in symptoms for x in ["skin", "rash", "acne"]):
        specialization = "Dermatology"

    elif any(x in symptoms for x in ["bone", "joint", "fracture"]):
        specialization = "Orthopedics"

    else:
        specialization = "General Physician"  # fallback

    return Doctor.query.filter_by(specialization=specialization).first()



@app.route('/book', methods=['GET', 'POST'])
def book():
    if 'user_id' not in session:
        return redirect('/login')

    selected_doctor_id = request.args.get('doctor_id')

    if request.method == 'POST':
        date = request.form['date']
        time = request.form['time']
        symptoms = request.form.get('symptoms', '')
        mode = request.form.get('mode', 'Offline')
        doctor_id = request.form.get('doctor_id')

        # 🔴 Auto-assign doctor if not selected manually
        if not doctor_id:
            doctor = assign_doctor(symptoms)
            if doctor:
                doctor_id = doctor.id
            else:
                flash("No doctor available for given symptoms.", "error")
                return redirect('/book')

        doctor_id = int(doctor_id)  # Ensure integer

        # Prevent past booking
        if date < datetime.today().strftime('%Y-%m-%d'):
            flash("Cannot book for past dates.", "error")
            return redirect('/book')

        # Prevent double booking
        if Appointment.query.filter_by(
            doctor_id=doctor_id,
            date=date,
            time=time
        ).first():
            flash("Slot already booked. Please choose another.", "error")
            return redirect('/book')

        # Generate Meet link if online
        meet_link = generate_meet_link() if mode == 'Online' else None

        appt = Appointment(
            patient_id=session['user_id'],
            doctor_id=doctor_id,
            date=date,
            time=time,
            symptoms=symptoms,
            mode=mode,
            meet_link=meet_link,
            status="Pending"
        )

        db.session.add(appt)
        db.session.commit()

        flash("Appointment Confirmed!", "success")
        return redirect(f'/receipt/{appt.id}')

    doctors = Doctor.query.all()
    return render_template('booking.html', doctors=doctors, selected_doctor_id=selected_doctor_id)


@app.route('/receipt/<int:id>')
def receipt(id):
    appt = Appointment.query.get_or_404(id)
    if appt.patient_id != session.get('user_id'): return redirect('/dashboard')
    return render_template('receipt.html', appt=appt)

@app.route('/cancel/<int:id>')
def cancel(id):
    appt = Appointment.query.get_or_404(id)
    if appt.patient_id == session.get('user_id'):
        db.session.delete(appt)
        db.session.commit()
        flash("Appointment cancelled successfully.", "info")
    return redirect('/dashboard')

# --- ADMIN ROUTES ---
@app.route('/admin')
def admin():
    if session.get('role') != 'admin': return redirect('/login')
    
    filter_date = request.args.get('date')
    query = Appointment.query
    if filter_date: query = query.filter_by(date=filter_date)
    appointments = query.order_by(Appointment.date.desc()).all()
    
    stats = {
        'total_patients': User.query.filter_by(role='patient').count(),
        'total_doctors': Doctor.query.count(),
        'total_appts': Appointment.query.count(),
        'revenue': Appointment.query.filter_by(status='Approved').count() * 500

    }
    
    status_counts = {
        'Pending': Appointment.query.filter_by(status='Pending').count(),
        'Approved': Appointment.query.filter_by(status='Approved').count(),
        'Rejected': Appointment.query.filter_by(status='Rejected').count()
    }
    
    return render_template('admin.html', appointments=appointments, stats=stats, status_counts=status_counts)

@app.route('/doctor/add', methods=['POST'])
def add_doctor():
    if session.get('role') == 'admin':
        db.session.add(Doctor(name=request.form['name'], specialization=request.form['spec'], experience=request.form['exp']))
        db.session.commit()
    return redirect('/admin')

@app.route('/doctor/delete/<int:id>')
def delete_doctor(id):
    if session.get('role') == 'admin':
        Doctor.query.filter_by(id=id).delete()
        db.session.commit()
    return redirect('/admin')

@app.route('/appointment/<action>/<int:id>')
def manage_appointment(action, id):
    if session.get('role') != 'admin': return redirect('/login')
    appt = Appointment.query.get(id)
    if action == 'approve': appt.status = 'Approved'
    elif action == 'reject': appt.status = 'Rejected'
    db.session.commit()
    return redirect('/admin')

@app.route('/export')
def export_csv():
    if session.get('role') != 'admin': return redirect('/login')
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['ID', 'Patient', 'Doctor', 'Date', 'Time', 'Status'])
    for a in Appointment.query.all():
        writer.writerow([a.id, a.patient.name, a.doctor.name, a.date, a.time, a.status])
    return Response(output.getvalue(), mimetype="text/csv", headers={"Content-Disposition": "attachment;filename=appointments.csv"})

if __name__ == "__main__":
    app.run(debug=True)