City Hospital – Appointment Management System
A professional, full-stack web application designed to automate hospital appointment scheduling, doctor management, and revenue tracking. This system replaces manual record-keeping with a streamlined digital workflow for both patients and healthcare administrators.

Built with efficiency by Kinza Zahra 🏥

Features
👤 Patient Portal
Secure Authentication: Register and login with session-based security and password hashing.

Smart Appointment Booking:

Auto-assign Doctor: Input symptoms (e.g., Fever, Headache, Chest Pain) and the system automatically assigns the correct specialist (e.g., General Physician).

Manual Selection: Browse the specialist list and choose your own doctor.

Online/Offline Modes: Choose between in-person visits or online consultations with auto-generated Google Meet links.

No Double Booking: Real-time validation prevents two patients from booking the same doctor at the same time.

Appointment Management: View your history, track status (Pending/Approved/Rejected), or cancel upcoming visits.

Digital Receipts: Download and print professional invoices for your records.

🛠 Admin Dashboard
Live Analytics: Monitor total patients, doctors, and appointments through a visual dashboard with status charts.

Doctor Directory: Add new specialists or remove existing ones to keep the hospital staff list updated.

Workflow Management: Approve or reject pending appointment requests with one click.

Revenue Tracking: Automatic calculation of hospital earnings based on approved appointments.

Data Portability: Export all appointment records to a CSV file for offline reporting.

💻 Tech Stack
Frontend: HTML5, CSS3 (Custom styling with Poppins font), JavaScript.

Backend: Python (Flask Framework).

Database: SQLite with SQLAlchemy ORM.

Security: Werkzeug (Password Hashing).

📂 Project Structure
Plaintext
Hospital-System/
│
├── app.py              # Application routes & core backend logic
├── models.py           # Database schema (User, Doctor, Appointment)
├── hospital.db         # SQLite database file
├── requirements.txt    # Python dependencies
│
├── static/             # Assets & Styling
│   ├── css/style.css
│   └── images/         # Local UI images
│
└── templates/          # Jinja2 HTML templates
    ├── base.html       # Shared layout (Navbar & Footer)
    ├── admin.html      # Admin dashboard
    ├── booking.html    # Appointment form
    └── receipt.html    # Invoice generator
⚙️ How to Run Locally
Clone the Repository:

Bash
git clone <your-repository-url>
cd Hospital-System
Install Dependencies:

Bash
pip install -r requirements.txt
Run the Application:

Bash
python app.py
Access the App:
Open your browser and go to http://127.0.0.1:5000.

🔑 Credentials & Logic
Default Admin: Email: admin@hospital.com | Password: admin123.

Pricing: All consultations are calculated at a fixed fee of ₹500.

🔮 Future Improvements
Integration with real online payment gateways.

Email and SMS confirmation alerts.

Advanced analytics dashboard for hospital performance.


Made with ❤️ by Kinza Zahra
