"""User models."""

# Config
from app.config.mysql_connection import connect_to_mysql


class User:
    """Modelo de la clase `User`."""

    def __init__(self, data: dict) -> None:
        """Constructor de la clase `User`."""
        
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def create(cls, data: dict):
        """
        Método encargado de guardar un usuario en la base de datos.

        Parámetros:
            - cls: Es una referencia a la clase.
            - data: Datos del usuario a guardar.
            
        Retorno:
            - bool: False si la consulta falla.
        """
        
        query = """
        INSERT INTO users (first_name, last_name, email, password) 
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        """
        return connect_to_mysql().query_db(query, data)
    
    @classmethod
    def get_by_id(cls, data: dict):
        """
        Método encargado de obtener un usuario de la base de datos.

        Parámetros:
            - cls: Es una referencia a la clase.
            - data: Datos del usuario a obtener.

        Retorno:
            - user (User): Objeto de la clase `User`.
        """
        
        query = """SELECT * FROM users WHERE id = %(id)s;"""
        results = connect_to_mysql().query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def get_by_email(cls, data: dict):
        """Obtener un usuario por su correo electrónico."""

        query = """SELECT * FROM users WHERE email = %(email)s;"""
        result = connect_to_mysql().query_db(query, data)
        
        if result:
            return cls(result[0])
        return None
