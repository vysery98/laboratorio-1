from flask import Blueprint, request, jsonify
from app.utils.logs import logEvent

score_bp = Blueprint("score", __name__)

@score_bp.route("/", methods=["POST"])
def calcularScore():
    data = request.get_json()

    edad = data.get("edad")
    ingresos = data.get("ingresos")

    if edad is None or ingresos is None:
        return jsonify({"error": "Debe ingresar todos los campos"}), 400

    # 👇 AHORA FUERA DEL IF (correcto)
    score = 0 

    if edad >= 25:
        score += 50
    else:
        score += 30

    if ingresos >= 1000:
        score += 50
    else:
        score += 20

    if score >= 80:
        riesgo = "bajo"
    elif score >= 60:
        riesgo = "medio"
    else:
        riesgo = "alto"

    # 🔥 AQUÍ SE EJECUTA BIEN
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
