Finance Tracker (Flask)

A simple web application for tracking personal income and expenses with user authentication.

This project was created as a university course project and later prepared as a portfolio project to demonstrate backend development basics.

✨ Features

User Authentication: Secure registration and login using Flask-Login.

Security: Password storage with hashing (Werkzeug).

Transaction Management: Add income and expense records.

Dashboard: Real-time calculation of total income, expenses, and current balance.

Data Protection: Users can only view and delete their own transactions.

Auto-setup: SQLite database initializes automatically on the first run.

📂 Project Structure

finance-tracker-flask/
├── app.py              # Main application logic and routes
├── db.py               # Database schema and initialization
├── requirements.txt    # List of dependencies
├── .gitignore          # Git exclusion file
├── .env.example        # Template for environment variables
└── templates/          # Jinja2 HTML templates
    ├── base.html       # Shared layout
    ├── login.html      # Login page
    ├── register.html   # Registration page
    └── dashboard.html  # User dashboard


🚀 How to Run Locally

1. Create a virtual environment

python -m venv .venv


2. Activate the environment

Windows:

.venv\Scripts\activate


macOS / Linux:

source .venv/bin/activate


3. Install dependencies

pip install -r requirements.txt


4. Run the application

python app.py


Open your browser at: http://127.0.0.1:5000

📊 Database

The application uses SQLite for simplicity. The database file and tables are created automatically when the script runs for the first time.

📝 Notes

This project is intended for educational and portfolio purposes. For a production environment, additional configuration (like CSRF protection and production WSGI server) would be required.

👤 Author

Sytsevich Roma