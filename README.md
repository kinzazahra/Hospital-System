🏥 **City Hospital – Appointment Management System**

A full-stack web application designed to modernize hospital operations by automating appointment scheduling, doctor management, and revenue tracking. This system replaces manual processes with an efficient, secure, and user-friendly digital workflow for both patients and administrators.

---

✨ **Features**

👤 **Patient Portal**

* **Secure Authentication**
  Register and log in securely using session-based authentication and password hashing.

* **Smart Appointment Booking**

  * **Auto-Assign Doctor:** Enter symptoms (e.g., fever, headache, chest pain), and the system automatically assigns the appropriate specialist.
  * **Manual Selection:** Browse available doctors and choose your preferred specialist.
  * **Flexible Consultation Modes:** Book either in-person visits or online consultations with auto-generated Google Meet links.

* **Real-Time Availability**
  Prevents double booking by ensuring no two patients can reserve the same doctor at the same time slot.

* **Appointment Management**
  View appointment history, track status (Pending / Approved / Rejected), and cancel upcoming bookings.

* **Digital Receipts**
  Generate, download, and print professional invoices for each appointment.

---

🛠 **Admin Dashboard**

* **Live Analytics**
  Track total patients, doctors, and appointments through an interactive dashboard with visual insights.

* **Doctor Management**
  Add or remove specialists to keep the hospital directory up to date.

* **Appointment Workflow**
  Approve or reject appointment requests instantly with a single click.

* **Revenue Tracking**
  Automatically calculate hospital earnings based on approved consultations.

* **Data Export**
  Download appointment records in CSV format for reporting and offline analysis.

---

💻 **Tech Stack**

* **Frontend:** HTML5, CSS3 (custom styling with Poppins), JavaScript
* **Backend:** Python (Flask Framework)
* **Database:** SQLite with SQLAlchemy ORM
* **Security:** Werkzeug (password hashing)

---

📂 **Project Structure**

```
Hospital-System/
│
├── app.py              # Core backend logic and routing
├── models.py           # Database models (User, Doctor, Appointment)
├── hospital.db         # SQLite database
├── requirements.txt    # Dependencies
│
├── static/
│   ├── css/style.css   # Styling
│   └── images/         # UI assets
│
└── templates/
    ├── base.html       # Common layout (navbar & footer)
    ├── admin.html      # Admin dashboard
    ├── booking.html    # Appointment booking page
    └── receipt.html    # Invoice template
```

---

⚙️ **How to Run Locally**

1. **Clone the Repository**

```
git clone <your-repository-url>
cd Hospital-System
```

2. **Install Dependencies**

```
pip install -r requirements.txt
```

3. **Run the Application**

```
python app.py
```

4. **Open in Browser**

```
http://127.0.0.1:5000
```

---

🔑 **Credentials & Pricing**

* **Admin Login**
  Email: [admin@hospital.com](mailto:admin@hospital.com)
  Password: admin123

* **Consultation Fee**
  Fixed at ₹500 per appointment

---

🔮 **Future Enhancements**

* Integration with online payment gateways
* Email and SMS notifications for bookings
* Advanced analytics and reporting dashboard

---

❤️ **Made with love by Kinza Zahra**
