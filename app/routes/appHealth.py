# Endpoint para verificar el estado del API
@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "service": "labratorio-1-api",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }), 200