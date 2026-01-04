Finance Tracker (Flask)

A web application for tracking personal income and expenses with user authentication. This project was developed as a university course project and refined for a portfolio to demonstrate backend development fundamentals.

Features

User Authentication: Secure registration and login functionality using Flask-Login.

Security: Password storage using cryptographic hashing via Werkzeug.

Transaction Management: Capability to add, view, and delete income and expense records.

Financial Dashboard: Automatic calculation of total income, expenses, and current balance.

Data Isolation: Users have access only to their own personal data.

Database Automation: Automatic SQLite database initialization on the first application launch.

Tech Stack

Language: Python

Framework: Flask

Database: SQLite

Authentication: Flask-Login

Templating: Jinja2

Styling: HTML5 / CSS3

Project Structure

finance-tracker-flask/
├── app.py              # Main application logic and routing
├── db.py               # Database connection and schema setup
├── requirements.txt    # Project dependencies
├── .gitignore          # Git exclusion rules
├── .env.example        # Environment variables template
└── templates/          # HTML templates folder
    ├── base.html       # Primary layout template
    ├── login.html      # Authentication page
    ├── register.html   # User registration page
    └── dashboard.html  # Main user interface


Installation and Setup

1. Environment Setup

Create a virtual environment to manage dependencies:

python -m venv .venv


2. Activation

Activate the virtual environment based on your operating system:

Windows:

.venv\Scripts\activate


macOS / Linux:

source .venv/bin/activate


3. Dependency Installation

Install the required Python packages:

pip install -r requirements.txt


4. Running the Application

Start the Flask development server:

python app.py


Access the application by navigating to: http://127.0.0.1:5000

Database Management

The application utilizes SQLite for data persistence. The database file and required tables are generated automatically during the first execution of app.py. No manual SQL configuration is required for local setup.

Security Considerations

This project is intended for educational purposes. For production deployments, ensure that:

A secure SECRET_KEY is defined in environment variables.

CSRF protection is fully implemented.

A production-grade WSGI server (e.g., Gunicorn) is used instead of the Flask built-in server.

Author

Sytsevich Roma