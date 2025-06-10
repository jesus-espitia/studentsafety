from flask import Flask, request, jsonify, render_template, session 
from flask_cors import CORS
from db import get_connection
from datetime import datetime

def verificar_directriz():
    data = request.get_json()
    documento = data.get('documento')

    if not documento:
        return jsonify({'success': False, 'message': 'Falta el documento en el QR'})

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM DIRECTRICES WHERE documento_directriz = %s", (documento,))
    directriz = cursor.fetchone()
    cursor.close()
    conn.close()

    if directriz:
        nombre_completo = f"{directriz['nombres_directriz']} {directriz['apellidos_directriz']}"
        session['nombre_admin'] = nombre_completo

        return jsonify({'success': True, 'message': 'Directriz verificada'})
    else:
        return jsonify({'success': False, 'message': 'No autorizado. QR no corresponde a una directriz'})
