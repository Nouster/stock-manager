import pymysql.cursors

class Product:
    def __init__(self, host='localhost', user='root', password='root', database='stock-manager', port=8889):
        self.connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

    def get_all_products(self):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT * FROM product;")
                products = cursor.fetchall()

                for product in products:
                    print(f"ID: {product['id']}, Name: {product['name']}, Reference: {product['reference']}, Quantity: {product['quantity']}")

        except pymysql.MySQLError as e:
            print(f"Erreur lors de la récupération des produits : {e}")

    def add_product(self, name, reference, quantity):
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