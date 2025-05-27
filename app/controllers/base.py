import mysql.connector

db = None

def init_db(app):
    global db
    db = mysql.connector.connect(
        host="localhost",
        user="tu_usuario_mysql",
        password="tu_contraseña_mysql",
        database="student_safety_db"
    )

def get_db():
    global db
    return db
