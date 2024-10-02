import pymysql.cursors

CONNECTION = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             database='stock-manager',
                             port=8889,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

cursor = CONNECTION.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS `stock-manager`;")
cursor.execute("USE `stock-manager`;")

cursor.execute("""
CREATE TABLE IF NOT EXISTS product(
  id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
  name VARCHAR(255) NOT NULL,
  reference VARCHAR(255) NOT NULL UNIQUE,
  quantity INT NOT NULL
) ENGINE=INNODB;
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS stock (
    stock_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    category VARCHAR(255) NOT NULL,
    incoming_quantity INT NOT NULL,
    outgoing_quantity INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    alert BOOLEAN NOT NULL,
    product_id INT,
    CONSTRAINT fk_product
        FOREIGN KEY (product_id) REFERENCES product(id)
        ON DELETE CASCADE
) ENGINE=INNODB;
""")

CONNECTION.commit()

cursor.close()
CONNECTION.close()
