import pymysql.cursors

CONNECTION = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             database='stock-manager',
                             port=8889,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    cursor = CONNECTION.cursor()

    cursor.execute("SELECT * FROM product;")
    products = cursor.fetchall()

    for product in products:
        print(f"ID: {product['id']}, Name: {product['name']}, Reference: {product['reference']}, Quantity: {product['quantity']}")

except pymysql.MySQLError as e:
    print(f"Erreur lors de la récupération des produits : {e}")

finally:
    cursor.close()


def add_product(name, reference, quantity):
    try:
        cursor = CONNECTION.cursor()
        cursor.execute("INSERT INTO product (name, reference, quantity) VALUES (%s, %s, %s)", 
                       (name, reference, quantity))
        CONNECTION.commit()  
        print(f"Produit '{name}' ajouté avec succès !")
    except pymysql.MySQLError as e:
        print(f"Erreur lors de l'ajout du produit : {e}")
    finally:
        cursor.close()


user_input = input('Souhaitez-vous ajouter un équipement ? (oui/non) : ')
if user_input.lower() == 'oui':
    equipment_name_input = input("Nom de l'équipement : ")
    equipment_reference_input = input("Référence du produit : ")
    equipment_quantity_input = input("Quantité à mettre en stock : ")

    try:
        equipment_quantity_input = int(equipment_quantity_input)  
        add_product(equipment_name_input, equipment_reference_input, equipment_quantity_input)
    except ValueError:
        print("Erreur : la quantité doit être un nombre entier.")
else:
    print("Aucun équipement ajouté.")

CONNECTION.close()
