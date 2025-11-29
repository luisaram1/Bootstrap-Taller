import os
from pathlib import Path

BASE = Path(__file__).resolve().parent

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "clave_super_secreta")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        f"sqlite:///{BASE/'database.sqlite3'}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
