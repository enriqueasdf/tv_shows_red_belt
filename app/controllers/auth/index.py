"""Index controller."""

# App config
from app import app

# Flask
from flask import render_template, session, redirect, url_for


@app.route("/")
def index():
    """Página de inicio."""

    # Proteger la ruta "/"
    if "user" in session:
        return redirect(url_for("shows"))

    return render_template("auth/index.html")
