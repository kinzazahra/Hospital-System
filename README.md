**City Hospital Appointment Management System**
A full-stack web application built using Flask and SQLite that allows patients to book hospital appointments and administrators to manage doctors, appointments, and revenue.

**🚀 Feature**
**Patient Module**
Registration & Login: Secure user authentication with password hashing.

Book Appointment: Choose between Online or Offline consultation modes.

Auto-Assign Doctor: Smart system that assigns a specialist based on symptoms like Fever, Headache, or Chest Pain.

Manual Selection: Option to manually select a preferred doctor from the list.

Double Booking Prevention: Logic to ensure time slots are not overbooked.

Appointment History: View past and upcoming appointments with their current status.

Download Receipt: Generate and print digital invoices for appointments.

**Admin Module**
Secure Dashboard: View statistics including total patients, total doctors, and total appointments.

Doctor Management: Add new specialists or delete existing ones from the database.

Appointment Approval: Review pending requests to approve or reject them.

Revenue Calculation: Automated tracking of hospital earnings based on approved appointments.

Data Export: Export all appointment data to a CSV file for reporting.

**🛠 Tech Stack**
Frontend: HTML, CSS, JavaScript.

Backend: Python (Flask Framework).

Database: SQLite with SQLAlchemy ORM.

Security: Werkzeug for password hashing and session-based authentication.

**📂 Project Structure**
Hospital-System/
│
├── app.py              # Application routes and backend logic
├── models.py           # Database models (User, Doctor, Appointment)
├── hospital.db         # SQLite database file
├── requirements.txt    # Python dependencies
│
├── templates/          # HTML templates (Jinja2)
│   ├── index.html
│   ├── login.html
│   ├── dashboard.html
│   └── receipt.html
│
└── static/             # Static assets
    ├── css/style.css
    └── images/
    
**⚙️ Installation & Setup**
Clone the Repository

git clone <your-repo-url>
cd Hospital-System
Install Dependencies

pip install -r requirements.txt
Run the Application

python app.py
Access the system at http://127.0.0.1:5000.

**🔑 Default Credentials**
Admin Email: admin@hospital.com

Admin Password: admin123

**💰 Revenue Logic**
Revenue is calculated as: Approved Appointments × Consultation Fee (Fixed at ₹500).
