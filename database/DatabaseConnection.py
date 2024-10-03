# database_connection.py
import pymysql.cursors

class DatabaseConnection:
    def __init__(self, host='localhost', user='root', password='root', database='stock-manager', port=8889):
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
