from flask import Blueprint, app, jsonify
from datetime import datetime

health_bp = Blueprint('health', __name__)

# Endpoint para verificar el estado del API
@health_bp.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "service": "labratorio-1-api",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }), 200