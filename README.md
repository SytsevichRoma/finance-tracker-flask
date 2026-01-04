# Finance Tracker (Flask)

A simple web application for tracking personal **income** and **expenses** with user authentication.

This project was created as a **university course project** and later prepared as a **portfolio project** to demonstrate backend development basics.

---

## Features
- User registration and login (Flask-Login)
- Secure password storage (password hashing)
- Add income and expense transactions
- Dashboard with total income, expenses and balance
- Delete user-owned transactions
- SQLite database with automatic initialization

---

## Tech Stack
- Python
- Flask
- Flask-Login
- SQLite
- Jinja2 (HTML templates)

---

## Project Structure
finance-tracker-flask/
│
├── app.py # Application logic, routes, authentication
├── db.py # Database connection and initialization
├── requirements.txt # Project dependencies
├── .gitignore
├── .env.example # Example environment variables
├── templates/ # HTML templates
│ ├── base.html
│ ├── login.html
│ ├── register.html
│ └── dashboard.html

yaml
Копіювати код

---

## How to Run Locally

### 1. Create virtual environment
```bash
python -m venv .venv
2. Activate it
Windows

bash
Копіювати код
.venv\Scripts\Activate
macOS / Linux

bash
Копіювати код
source .venv/bin/activate
3. Install dependencies
bash
Копіювати код
pip install -r requirements.txt
4. Run the application
bash
Копіювати код
python app.py
Open in browser:

cpp
Копіювати код
http://127.0.0.1:5000
Database
The application uses SQLite for simplicity.
Database tables are created automatically on first run.

Notes
This project is intended for educational and portfolio purposes.
In a production environment, additional security and configuration would be required.

Author
Sytsevich Roma