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
    CONNECTION.close()
