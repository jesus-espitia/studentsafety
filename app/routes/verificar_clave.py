from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from db import get_connection
from datetime import datetime

def verificar_clave():
    data = request.get_json()
    documento = data.get('documento')
    clave = data.get('clave')

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT clave_directriz FROM DIRECTRICES WHERE documento_directriz = %s", (documento,))
    directriz = cursor.fetchone()
    cursor.close()
    conn.close()

    if directriz and directriz['clave_directriz'] == clave:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'message': 'Clave incorrecta'})