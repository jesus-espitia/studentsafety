from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from db import get_connection
from datetime import datetime

def api_grupos():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT g.id_grado_grado AS id, g.grado_grupo AS grado, 
           CONCAT(d.nombres_directriz, ' ', d.apellidos_directriz) AS director
    FROM GRADO_GRUPO g
    JOIN DIRECTRICES d ON g.director_id = d.id_directrices
    """
    cursor.execute(query)
    grupos = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(grupos)