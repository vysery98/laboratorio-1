# Importación de librerías
from flask import Blueprint, request, jsonify
# Importación de rutas
from app.utils.logs import logEvent

# Definición de Blueprint
score_bp = Blueprint("score", __name__)

@score_bp.route("/", methods=["POST"])
def calcularScore():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No se enviaron datos"}), 400

    edad = data.get("edad")
    ingresos = data.get("ingresos")

    if edad is None or ingresos is None:
        return jsonify({"error": "Debe ingresar todos los campos"}), 400

    # Valor por defecto de score
    score = 0 

    if edad >= 25:
        score += 50
    else:
        score += 30

    if ingresos >= 1000:
        score += 50
    else:
        score += 20

    # Calificación de Riesgo
    if score >= 80:
        riesgo = "bajo"
    elif score >= 60:
        riesgo = "medio"
    else:
        riesgo = "alto"

    # Registro de Log
    logEvent("scoring", {
        "edad": edad,
        "ingresos": ingresos,
        "score": score,
        "riesgo": riesgo
    })

    return jsonify({
        "score": score,
        "riesgo": riesgo
    }), 200
