"""Show model."""

# Config
from app.config.mysql_connection import connect_to_mysql

# Models
from app.models.user import User


class Show:
    """Modelo de la clase `Show`."""

    def __init__(self, data: dict) -> None:
        """Constructor de la clase `Show`."""

        self.id = data["id"]
        self.title = data["title"]
        self.network = data["network"]
        self.release_date = data["release_date"]
        self.description = data["description"]
        self.user_id = data["user_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        """
        Método de clase encargado de obtener todos los shows desde la base de
        datos.

        Parámetros:
            - cls: Es una referencia a la clase.

        Retorno:
            - shows (list): Lista de objetos de la clase `Show`
        """

        query = """SELECT * FROM shows;"""
        results = connect_to_mysql().query_db(query)
        shows: list = []
        for show in results:
            shows.append(show)
        return shows

    @classmethod
    def create(cls, data: dict):
        """
        Método de clase encargado de guardar un show en la base de datos.

        Parámetros:
            - cls: Es una referencia a la clase.
            - data (dict): Datos del show a guardar.
        
        Retorno:
            - bool: False si la consulta falla.
        """

        query = """
        INSERT INTO shows (title, network, release_date, description, user_id)
        VALUES (%(title)s, %(network)s, %(release_date)s, %(description)s, %(user_id)s);
        """
        return connect_to_mysql().query_db(query, data)

    @classmethod
    def delete(cls, data: dict):
        """
        Método de clase encargado de eliminar un show en la base de datos.

        Parámetros:
            - cls: Es una referencia a la clase.
            - data (dict): Datos del show a eliminar.
        
        Retorno:
            - bool: False si la consulta falla.
        """

        query = """DELETE FROM shows WHERE id = %(id)s;"""
        return connect_to_mysql().query_db(query, data)
    
    @classmethod
    def get_by_id(cls, data: dict):
        """
        Método de clase encargado de obtener un show en la base de datos.

        Parámetros:
            - cls: Es una referencia a la clase.
            - data (dict): Datos del show a obtener.
        
        Retorno:
            - show (Show): Objeto de la clase `Show`.
        """

        query = """
        SELECT * FROM shows
        INNER JOIN users ON shows.user_id = users.id
        WHERE shows.id = %(id)s;
        """
        results = connect_to_mysql().query_db(query, data)

        # Construir el objeto de las clase `Show` y `User`
        show = cls(results[0])
        show.user = User(results[0])
        return show
