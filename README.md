🏥 Hospital Appointment Management System

A full-stack web application built using Flask (Python) and SQLite that allows patients to book hospital appointments and administrators to manage doctors, appointments, and revenue.

This project was developed as part of an internship to demonstrate practical full-stack development and database integration.

🚀 Features
👤 Patient

Register & Login

Book Appointment (Online / Offline)

Auto-assign doctor based on symptoms

Manual doctor selection

Prevent double booking

View appointment history

Cancel appointment

Download appointment receipt

🛠 Admin

Secure admin login

Add/Delete doctors

Approve / Reject appointments

View dashboard statistics

Revenue calculation

Export appointments as CSV

📩 Contact System

Patients can send messages

Messages stored in database

Flash notifications for confirmation

🧠 Smart Features

Automatic doctor assignment for:

Fever

Headache

Chest pain
→ Assigned to General Physician

Google Meet link generation for online consultation

Role-based authentication

Secure password hashing

Session management

🛠 Tech Stack

Frontend

HTML

CSS

JavaScript

Backend

Python (Flask)

Database

SQLite

ORM

SQLAlchemy

Security

Werkzeug (Password Hashing)

🗂 Project Structure
Hospital-System/
│
├── app.py
├── models.py
├── hospital.db
├── requirements.txt
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── booking.html
│   ├── admin.html
│   ├── receipt.html
│
├── static/
│   ├── css/
│   └── js/

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Application
python app.py


Open browser:

http://127.0.0.1:5000

🔑 Default Admin Credentials

Email:

admin@hospital.com


Password:

admin123

💰 Revenue Logic

Revenue is calculated as:

Approved Appointments × Consultation Fee


(Current consultation fee: ₹500)

🛡 Security Implemented

Password hashing

Role-based route protection

Session-based login

Validation for past date booking

Prevention of double booking

📌 Limitations

No real payment gateway integration

No email notifications

🔮 Future Improvements

Payment gateway integration

Email & SMS notifications

Doctor availability scheduling

Advanced analytics




