"""Login controller."""

# App config
from app import app

# Flask
from flask import request, redirect, url_for, flash, session

# Models
from app.models.user import User

# Bcrypt
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)



@app.route("/login/", methods=["POST"])
def login():
    """Procesar formulario de inicio de sesión."""

    # Recuperamos los datos desde el formulario
    email = request.form["email"]
    password = request.form["password"]

    # Validamos que el usuario exista
    data = {"email": email}
    user = User.get_by_email(data)

    if not user:
        flash("User not found", "danger")
        return redirect(url_for("index"))

    # Validamos que la contraseña sea correcta
    check_password = bcrypt.check_password_hash(user.password, password)
    if check_password:
        session["user"] = {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email
        }
        flash("Login successful", "success")
    else:
        flash("Hmmm... Something went wrong", "danger")
        return redirect(url_for("index"))

    return redirect(url_for("shows"))
