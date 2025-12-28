import psycopg
from dotenv import load_dotenv
import os
import pytest

load_dotenv()
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD")
}

@pytest.fixture
def db_conn():
    conexion = psycopg.connect(
        host = DB_CONFIG["host"],
        dbname= DB_CONFIG["dbname"],
        user = DB_CONFIG["user"],
        password= DB_CONFIG["password"]
        )

    conexion.autocommit = False

    yield conexion

    conexion.rollback()
    conexion.close()
    
    
    

