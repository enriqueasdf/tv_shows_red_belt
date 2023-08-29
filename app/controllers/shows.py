"""Show controllers."""

# App config
from app import app

# Flask
from flask import render_template, session, redirect, url_for, request, flash

# Models
from app.models.show import Show


@app.route("/shows/")
def shows():
    """
    TODO: Función show.
    """

    # Proteger la ruta "/shows/"
    if "user" not in session:
        return redirect(url_for("index"))
    
    shows = Show.get_all()
    return render_template("shows/index.html", shows=shows)


@app.route("/shows/new/", methods=["GET", "POST"])
def create_show():
    """
    TODO: Función create_show.
    """

    # Proteger la ruta "/shows/new/"
    if "user" not in session:
        return redirect(url_for("index"))
    
    # Si el método HTTP es POST
    if request.method == "POST":
        # Crear un nuevo show
        data = {
            "title": request.form["title"],
            "network": request.form["network"],
            "description": request.form["description"],
            "release_date": request.form["release_date"],
            "user_id": session["user"]["id"]
        }
        if Show.create(data):
            flash("Show created successfully", "success")
            return redirect(url_for("shows"))
        else:
            flash("Hmmm... something went wrong", "danger")
    
    return render_template("shows/create_show.html")


@app.route("/shows/<int:show_id>/")
def read_show(show_id: int):
    """
    Función encargada de obtener un show de la base de datos.

    Parámetros:
        - show_id (int): ID del show a obtener.

    Retorno:
        - render_template: Renderiza la vista de show.
    """

    # Proteger la ruta "/shows/<int:show_id>/"
    if "user" not in session:
        return redirect(url_for("index"))
    
    # Obtener el show
    data = {"id": show_id}
    show = Show.get_by_id(data)
    return render_template("shows/read_show.html", show=show)


@app.route("/shows/<int:show_id>/delete/")
def delete_show(show_id: int):
    """
    Función encargada de eliminar un show de la base de datos.

    Parámetros:
        - show_id (int): ID del show a eliminar.

    Retorno:
        - redirect: Redirecciona a la vista shows.
    """

    # Proteger la ruta "/shows/<int:show_id>/delete/"
    if "user" not in session:
        return redirect(url_for("index"))
    
    # Eliminar el show
    data = {"id": show_id}
    if Show.delete(data) is None:
        flash("Show deleted successfully", "success")
    else:
        flash("Hmmm... something went wrong", "danger")

    return redirect(url_for("shows"))
