import pymysql.cursors

def conectar_db():
    return  pymysql.connect(
        host='localhost',
        user='root',
        password='root_password',
        database='crud',
        cursorclass=pymysql.cursors.DictCursor,
        port=3306,
    )