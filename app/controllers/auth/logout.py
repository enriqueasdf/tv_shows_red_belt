"""Logout controller."""

# App config
from app import app

# Flask
from flask import redirect, url_for, flash, session


@app.route("/logout/")
def logout():
    """Cerrar sesión del usuario."""

    # Proteger la ruta "/logout/"
    if "user" not in session:
        return redirect(url_for("index"))

    session.clear()
    flash("Closed session without problems", "info")
    return redirect(url_for("index"))