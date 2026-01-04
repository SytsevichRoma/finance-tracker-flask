from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

from db import get_db, init_db

app = Flask(__name__)
app.secret_key = "dev-secret-change-me"

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

init_db()

class User(UserMixin):
    def __init__(self, user_id: int, email: str):
        self.id = user_id
        self.email = email

@login_manager.user_loader
def load_user(user_id: str):
    with get_db() as con:
        row = con.execute("SELECT id, email FROM users WHERE id = ?", (int(user_id),)).fetchone()
    if not row:
        return None
    return User(row["id"], row["email"])

@app.get("/")
def index():
    return redirect(url_for("dashboard")) if current_user.is_authenticated else redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        if not email or not password:
            flash("Введи email і пароль.")
            return redirect(url_for("register"))
        if len(password) < 6:
            flash("Пароль мінімум 6 символів.")
            return redirect(url_for("register"))
        pw_hash = generate_password_hash(password)
        try:
            with get_db() as con:
                con.execute("INSERT INTO users(email, password_hash) VALUES (?, ?)", (email, pw_hash))
            flash("Акаунт створено! Тепер увійди.")
            return redirect(url_for("login"))
        except Exception:
            flash("Такий email вже існує.")
            return redirect(url_for("register"))
    return render_template("register.html", app_name="finance tracker")

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        with get_db() as con:
            row = con.execute("SELECT id, email, password_hash FROM users WHERE email = ?", (email,)).fetchone()
        if not row or not check_password_hash(row["password_hash"], password):
            flash("Невірний email або пароль.")
            return redirect(url_for("login"))
        login_user(User(row["id"], row["email"]))
        return redirect(url_for("dashboard"))
    return render_template("login.html", app_name="finance tracker")

@app.get("/logout")
@login_required
def logout():
    logout_user()
    flash("Ти вийшов з акаунта.")
    return redirect(url_for("login"))

@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    if request.method == "POST":
        kind = request.form.get("kind", "expense")
        amount_str = request.form.get("amount", "0").replace(",", ".")
        note = (request.form.get("note", "") or "").strip()
        tdate = request.form.get("tdate", date.today().isoformat())
        if kind not in ("income", "expense"):
            flash("Невірний тип операції.")
            return redirect(url_for("dashboard"))
        try:
            amount = float(amount_str)
            if amount <= 0:
                raise ValueError
        except ValueError:
            flash("Сума має бути числом > 0.")
            return redirect(url_for("dashboard"))
        with get_db() as con:
            con.execute(
                "INSERT INTO transactions(user_id, kind, amount, tdate, note) VALUES (?, ?, ?, ?, ?)",
                (int(current_user.id), kind, amount, tdate, note if note else None),
            )
        flash("Операцію додано.")
        return redirect(url_for("dashboard"))
    with get_db() as con:
        items = con.execute(
            "SELECT id, kind, amount, tdate, note FROM transactions WHERE user_id=? ORDER BY tdate DESC, id DESC",
            (int(current_user.id),),
        ).fetchall()
        income = con.execute(
            "SELECT COALESCE(SUM(amount), 0) AS s FROM transactions WHERE user_id=? AND kind='income'",
            (int(current_user.id),),
        ).fetchone()["s"]
        expense = con.execute(
            "SELECT COALESCE(SUM(amount), 0) AS s FROM transactions WHERE user_id=? AND kind='expense'",
            (int(current_user.id),),
        ).fetchone()["s"]
    balance = float(income) - float(expense)
    return render_template(
        "dashboard.html",
        app_name="finance tracker",
        items=items,
        income=income,
        expense=expense,
        balance=balance,
        today=date.today().isoformat(),
    )

@app.post("/transactions/<int:tid>/delete")
@login_required
def delete_transaction(tid: int):
    with get_db() as con:
        con.execute("DELETE FROM transactions WHERE id=? AND user_id=?", (tid, int(current_user.id)))
    flash("Видалено.")
    return redirect(url_for("dashboard"))

if __name__ == "__main__":
    app.run(debug=True)
