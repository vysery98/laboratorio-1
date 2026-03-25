# Importación de Librerías
from flask import Blueprint, request, jsonify
# Importación de rutas
from app.models.db import getConnection
from app.utils.logs import logEvent

# Definición de Blueprint
auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods = ["POST"])
# Función - Gestión de login de users
def login():
    # Extracción de datos para petición
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # Validación - campos obligatorios
    if not username or not password:
        return jsonify({"error": "Por favor, ingrese las credenciales."}), 400

    # Conexión a bd para validación de usuario
    conn = getConnection()
    cursor = conn.cursor()

    # Consulta parametrizada
    cursor.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (username, password)
    )

    user = cursor.fetchone()
    conn.close()

    # Validación de salida
    if user: # Ingreso exitoso en Log
        logEvent("login", {"usuario": username, "resultado": "OK"})
        return jsonify({"message": "Acceso exitoso"}), 200
    else: # Intento fallido en Log
        logEvent("login", {"usuario": username, "resultado": "ERROR"})
        return jsonify({"error": "Credenciales incorrectas, intente nuevamente"}), 401