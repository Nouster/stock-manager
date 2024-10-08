import pymysql.cursors
from model.interface.ITableOperation import ITableOperation

class Product(ITableOperation):
    def __init__(self, db_connection):
        self.connection = db_connection.get_connection()

    def get_all_entries(self):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT * FROM product;")
                products = cursor.fetchall()

                for product in products:
                    print(f"ID: {product['id']}, Name: {product['name']}, Reference: {product['reference']}, Quantity: {product['quantity']}")

        except pymysql.MySQLError as e:
            print(f"Erreur lors de la récupération des produits : {e}")

    def add_entry(self, name, reference, quantity):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("INSERT INTO product (name, reference, quantity) VALUES (%s, %s, %s)", 
                               (name, reference, quantity))
                self.connection.commit()  
                print(f"Produit '{name}' ajouté avec succès !")

        except pymysql.MySQLError as e:
            print(f"Erreur lors de l'ajout du produit : {e}")

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Connexion à la base de données fermée.")
