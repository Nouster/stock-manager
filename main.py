from model.Product import Product
from database.DatabaseConnection import DatabaseConnection
from database.DatabaseCreation import DatabaseCreation

createDatabase = input('Voulez-vous créer la base de données \n')

if createDatabase.lower() == 'oui':
    DatabaseCreation.createDatabase()

db_connection = DatabaseConnection()

product_manager = Product(db_connection)

user_input = input("Souhaitez-vous consulter la liste des équipements : \n")

if user_input.lower() == "oui":
    product_manager.get_all_entries()

user_input = input("Souhaitez-vous ajouter des produits : \n")
if user_input.lower() == "oui":
    user_input_name = input("Quel nom pour votre produit : \n")
    user_input_reference = input("Quel référence pour votre produit : \n")
    user_input_quantity = input("Quelle quantité à ajouter : \n")
    
    product_manager.add_entry(user_input_name, user_input_reference, int(user_input_quantity))

db_connection.close_connection()