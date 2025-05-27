from flask import Flask, render_template
from app.controllers.base import get_db
import os

# Crear la app Flask
app = Flask(__name__, template_folder='app/templates', static_folder='app/static')

app.config['TEMPLATES_AUTO_RELOAD'] = True

# === Rutas ===
@app.route('/')
def index():
    return render_template("login_admin.html")  # Vista protegida por acceso QR real

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/usuarios')
def usuarios():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    cursor.close()
    db.close()
    return render_template("usuarios.html", usuarios=usuarios)

@app.route('/egresados')
def egresados():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM egresados")
    egresados = cursor.fetchall()
    cursor.close()
    db.close()
    return render_template("egresados.html", egresados=egresados)

@app.route('/citas')
def citas():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM citas")
    citas = cursor.fetchall()
    cursor.close()
    db.close()
    return render_template("citas.html", citas=citas)

@app.route('/asistencias')
def asistencias():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM asistencias")
    asistencias = cursor.fetchall()
    cursor.close()
    db.close()
    return render_template("asistencias.html", asistencias=asistencias)

# === Ejecutar el servidor ===
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)
