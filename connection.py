import pymysql.cursors

CONNECTION = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='stock-manager',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)