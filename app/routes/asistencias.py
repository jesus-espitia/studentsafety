from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from db import get_connection
from datetime import datetime


def ver_asistencias():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    # Obtener todos los grados/grupos disponibles
    cursor.execute("""
        SELECT GG.id_grado_grado, GG.grado_grupo, D.nombres_directriz, D.apellidos_directriz
        FROM GRADO_GRUPO GG
        JOIN DIRECTRICES D ON GG.director_id = D.id_directrices
    """)
    grupos = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('ver_asistencias.html', grupos=grupos)

def consultar_asistencias():
    grupo_id = request.args.get('grupo_id')

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT A.fechaHora, P.nombres_persona, P.apellidos_persona, GG.grado_grupo,
               D.nombres_directriz, D.apellidos_directriz
        FROM ASISTENCIA A
        JOIN PERSONAS P ON A.persona_id = P.documento_persona
        JOIN GRADO_GRUPO GG ON P.grado_grupo_id = GG.id_grado_grado
        JOIN DIRECTRICES D ON GG.director_id = D.id_directrices
        WHERE GG.id_grado_grado = %s
        ORDER BY A.fechaHora DESC
    """, (grupo_id,))
    asistencias = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('asistencias_tabla.html', asistencias=asistencias)
