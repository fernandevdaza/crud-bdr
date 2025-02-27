import pymysql

def conectar_db():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='root_password',
        database='crud',
        cursorclass=pymysql,
        port=3306,
    )