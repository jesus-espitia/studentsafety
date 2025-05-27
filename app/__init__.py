from flask import Flask
from app.controllers.base import init_db

def create_app():
    app = Flask(__name__)
    app.secret_key = "clave_super_segura"

    # Inicializar base de datos
    init_db(app)

    # Registrar rutas
    from app.routes import qr_scanner, admin_panel
    app.register_blueprint(qr_scanner.bp)
    app.register_blueprint(admin_panel.bp)

    return app
