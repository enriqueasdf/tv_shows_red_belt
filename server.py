"""Server app."""

# App config
from app import app

# Auth controllers
from app.controllers.auth.index import index
from app.controllers.auth.login import login
from app.controllers.auth.logout import logout
from app.controllers.auth.register import register

# Shows controllers
from app.controllers.shows import shows, create_show, delete_show, read_show


# Run
if __name__ == "__main__":
    app.run(debug=True, port=5000)
