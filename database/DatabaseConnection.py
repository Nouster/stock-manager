from dotenv import load_dotenv
import os
import pymysql.cursors
from database.AbstractDatabaseConnection import AbstractDatabaseConnection


load_dotenv()

class DatabaseConnection (AbstractDatabaseConnection):
    def __init__(self):
        host = os.getenv('DB_HOST')
        user = os.getenv('DB_USER')
        password = os.getenv('DB_PASSWORD')
        database = os.getenv('DB_DATABASE')
        port = int(os.getenv('DB_PORT'))

        self.connection = None
        try:
            self.connection = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                port=port,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            print("Connexion à la base de données établie.")
        except pymysql.MySQLError as e:
            print(f"Erreur lors de la connexion à la base de données : {e}")

    def get_connection(self):
        return self.connection

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Connexion à la base de données fermée.")
