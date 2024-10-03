import pymysql.cursors


class databaseCreation:
        
    @staticmethod
    def createDatabase():
        CONNECTION = pymysql.connect(host='localhost',
                                    user='root',
                                    password='root',
                                    database='stock-manager',
                                    port=8889,
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)

        cursor = CONNECTION.cursor()

        with open('database.sql', 'r') as file:
            sql_script = file.read()

        sql_commands = sql_script.split(';')

        for command in sql_commands:
            if command.strip():  
                cursor.execute(command)

        CONNECTION.commit()

        cursor.close()
        CONNECTION.close()
