from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from db import get_connection
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrar_asistencia', methods=['POST'])
def registrar_asistencia():
    try:
        data = request.get_json()
        tipo = data.get('tipo')
        documento = data.get('documento')
        nota = data.get('nota')

        if not tipo or not documento:
            return jsonify({'success': False, 'message': 'Datos incompletos en el QR.'})

        conn = get_connection()
        cursor = conn.cursor()

        # Buscar persona en base de datos
        cursor.execute("""
            SELECT id_personas, nombres_persona, apellidos_persona
            FROM PERSONAS
            WHERE documento_persona = %s AND tipo_personas = %s
        """, (documento, tipo))
        persona = cursor.fetchone()

        if not persona:
            return jsonify({'success': False, 'message': 'Persona no encontrada en la base de datos.'})

        id_persona, nombres, apellidos = persona

        # Registrar asistencia
        cursor.execute("""
            INSERT INTO ASISTENCIA (fechaHora, persona_id)
            VALUES (%s, %s)
        """, (datetime.now(), id_persona))
        conn.commit()

        return jsonify({'success': True, 'message': f'¡Bienvenido/a {nombres} {apellidos}! Asistencia registrada. <br> Recuerda {nota}'})

    except Exception as e:
        print("ERROR:", e)
        return jsonify({'success': False, 'message': 'Error en el servidor.'})
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()

if __name__ == '__main__':
    app.run(debug=True)
