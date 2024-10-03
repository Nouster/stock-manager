from dotenv import load_dotenv
import os
import pymysql.cursors

load_dotenv()

class DatabaseConnection:
    def __init__(self):
        host = os.getenv('DB_HOST', 'localhost')
        user = os.getenv('DB_USER', 'root')
        password = os.getenv('DB_PASSWORD', 'root')
        database = os.getenv('DB_DATABASE', 'stock-manager')
        port = int(os.getenv('DB_PORT', 8889))

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
