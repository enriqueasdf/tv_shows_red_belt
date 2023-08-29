"""Register controller."""

# App config
from app import app

# Flask
from flask import request, redirect, url_for, flash

# Models
from app.models.user import User

# Bcrypt
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route("/register/", methods=["POST"])
def register():
    """Procesar formulario de registro."""

    # Recuperamos los datos desde el formulario
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    password = request.form["password"]
    password_confirm = request.form["password_confirm"]

    # Validamos que el usuario no exista
    data = {"email": email}
    user = User.get_by_email(data)

    if user:
        flash("Usuario ya existe", "danger")
        return redirect(url_for("index"))

    # Validamos que las contraseñas coincidan
    if password != password_confirm:
        flash("La contraseña no coinciden", "warning")
        return redirect(url_for("index"))

    password_hash = bcrypt.generate_password_hash(password)
    result = User.create({
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password_hash
    })

    if result:
        flash("User registered successfully", "success")
    else:   
        flash("Hmmm... Something went wrong", "danger")

    return redirect(url_for("index"))