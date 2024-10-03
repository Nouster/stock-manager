from model.Product import Product
from database.DatabaseCreation import DatabaseCreation

createDatabase = input('Souhaitez-vous créer la base de données \n')

if createDatabase.lower == 'oui':
    DatabaseCreation.createDatabase()

product_manager = Product()

user_input = input("Souhaitez-vous consulter la liste des équipements : \n")

if user_input.lower() == "oui":
    product_manager.get_all_products()

user_input = input("Souhaitez-vous ajouter des produits : \n")
if user_input.lower() == "oui":
    user_input_name = input("Quel nom pour votre produit : \n")
    user_input_reference = input("Quel référence pour votre produit : \n")
    user_input_quantity = input("Quelle quantité à ajouter : \n")
    int(user_input_quantity)

    product_manager.add_product(user_input_name,user_input_reference,user_input_quantity)