# Finance Tracker (Flask)

Simple web application for tracking personal income and expenses.

The project was created as a **university course project** and demonstrates
basic backend development with authentication and database interaction.

## Features
- User registration and login (Flask-Login)
- Add income and expense transactions
- Dashboard with totals: income, expenses, balance
- Delete own transactions
- SQLite database with automatic initialization

## Tech Stack
- Python
- Flask
- Flask-Login
- SQLite
- Jinja2 templates

## Project Structure
- `app.py` — application logic, routes, authentication
- `db.py` — database connection and initialization
- `templates/` — HTML templates

## How to run

Create virtual environment:
```bash
python -m venv .venv
Activate it:

Windows

bash
Копіювати код
.venv\Scripts\Activate
macOS / Linux

bash
Копіювати код
source .venv/bin/activate
Install dependencies:

bash
Копіювати код
pip install -r requirements.txt
Run the app:

bash
Копіювати код
python app.py
Open in browser:

cpp
Копіювати код
http://127.0.0.1:5000
Screenshots
(Add screenshots here after upload)

Notes
This project uses SQLite for simplicity.
In a production environment, a more robust database and environment configuration would be used.