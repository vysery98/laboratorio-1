# Importación de librerías
from flask import Flask

# Importación de rutas
from app.routes.appHealth import health_bp
from app.routes.auth import auth_bp
from app.routes.scoreCredit import score_bp

def create_app():
    app = Flask(__name__)

    # Registro de rutas
    app.register_blueprint(health_bp, url_prefix = "/health")
    app.register_blueprint(auth_bp, url_prefix = "/auth")
    app.register_blueprint(score_bp, url_prefix = "/score")

    return app

# Creación de App
app = create_app()

'''
Punto de entrada de la app. El servidor solo se ejecuta si el archivo se
ejecuta directamente
'''
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8080) 