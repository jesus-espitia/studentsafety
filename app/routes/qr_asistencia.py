from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from db import get_connection
from datetime import datetime


def registrar_asistencia():
    try:
        data = request.get_json()
        tipo = data.get('tipo')
        documento = data.get('documento')
        nombres = data.get('nombres')
        apellidos = data.get('apellidos')

        if not tipo or not documento:
            return jsonify({'success': False, 'message': 'Datos incompletos en el QR.'})

        conn = get_connection()
        cursor = conn.cursor()

        # Buscar persona en base de datos por documento_persona
        cursor.execute("""
            SELECT documento_persona, nombres_persona, apellidos_persona
            FROM PERSONAS
            WHERE documento_persona = %s AND tipo_personas = %s
        """, (documento, tipo))
        persona = cursor.fetchone()

        if not persona:
            return jsonify({'success': False, 'message': 'Persona no encontrada en la base de datos.'})

        documento_persona, nombres, apellidos = persona

        # Registrar asistencia con documento_persona como clave foránea
        cursor.execute("""
            INSERT INTO ASISTENCIA (fechaHora, persona_id, nombres_asistencia, apellidos_asistencia)
            VALUES (%s, %s, %s, %s)
        """, (datetime.now(), documento_persona, nombres, apellidos))
        conn.commit()

        return jsonify({'success': True, 'message': f'¡Bienvenido/a {nombres} {apellidos}! Asistencia registrada.'})

    except Exception as e:
        print("ERROR:", e)
        return jsonify({'success': False, 'message': 'Error en el servidor.'})
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()