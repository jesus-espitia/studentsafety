from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# Ruta principal que sirve el HTML
@app.route('/')
def index():
    return render_template('index.html')

# Ruta que recibe los datos del QR y registra la asistencia
@app.route('/registrar_asistencia', methods=['POST'])
def registrar_asistencia():
    try:
        data = request.get_json()
        tipo = data.get('tipo')
        documento = data.get('documento')

        if not tipo or not documento:
            return jsonify({'success': False, 'message': 'Datos incompletos en el QR.'})

        # Conexión a MySQL
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="student_safety_db"
        )
        cursor = conn.cursor()

        # Verifica si el usuario existe
        cursor.execute("SELECT nombre FROM usuarios WHERE numero_documento = %s AND tipo = %s", (documento, tipo))
        result = cursor.fetchone()
        if not result:
            return jsonify({'success': False, 'message': 'Usuario no encontrado en la base de datos.'})

        nombre = result[0]

        # Registra la asistencia
        cursor.execute("INSERT INTO asistencias (documento_usuario, tipo_usuario) VALUES (%s, %s)", (documento, tipo))
        conn.commit()

        return jsonify({'success': True, 'message': f'¡Bienvenido/a {nombre}! Asistencia registrada.'})

    except Exception as e:
        print(e)
        return jsonify({'success': False, 'message': 'Error en el servidor.'})
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

if __name__ == '__main__':
    app.run(debug=True)
