# Importación de librería - Simulación DB
import sqlite3

# Nombre del archivo (bd local)
dbName = "database.db"

def getConnection():
    conn = sqlite3.connect(dbName)
    # Acceso a la data como diccionarios
    conn.row_factory = sqlite3.Row
    return conn

def initDb(): # Crea la tabla y usuario adm
    conn = getConnection() # Abre la base
    cursor = conn.cursor()

    # Creación tabla Users - autenticación
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)

    # Validación y creación de user de prueba
    cursor.execute("SELECT * FROM users WHERE username = 'admin'")
    if not cursor.fetchone():
        # Pwd se debería hashear - PROD
        cursor.execute(
            "INSERT INTO users (username, password) VALUES(?, ?)",
            ("admin", "1234")
        )
    
    # Guardado de cambios y cierre de conexión
    conn.commit()
    conn.close()