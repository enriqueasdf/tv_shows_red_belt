"""App config."""

# Standard libraries
import os

# Flask
from flask import Flask

# Python-dotenv
from dotenv import load_dotenv


#Instancia de Flask
app = Flask(__name__)

# Secret key
app.secret_key = os.getenv("SECRET_KEY")

# Load Python-dotenv
load_dotenv()
