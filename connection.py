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

CONNECTION.commit()
cursor.close()
CONNECTION.close()


# with open('database.sql', 'r') as file:
#     sql_script = file.read()

# sql_commands = sql_script.split(';')

# for command in sql_commands:
#     if command.strip():  
#         cursor.execute(command)

# CONNECTION.commit()

