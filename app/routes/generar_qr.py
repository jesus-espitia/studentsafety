#import mysql.connector
#from flask_cors import CORS
#from db import get_connection
#from datetime import datetime
#from flask import Flask, request, jsonify, render_template
#from flask import send_file
#import qrcode
#import json
#from io import BytesIO
#
#def generar_qr_pa():
#    connection = get_connection()
#    estudiantes = []
#    directrices = []
#
#    if request.method == 'POST':
#        tipo = request.form.get('tipo')
#        documento = request.form.get('documento')
#        nombres = request.form.get('nombres')
#        apellidos = request.form.get('apellidos')
#
#        qr_data = {
#            "tipo": tipo,
#            "documento": documento,
#            "nombres": nombres,
#            "apellidos": apellidos
#        }
#
#        if tipo == "directriz":
#            clave = request.form.get('clave')
#            cargo = "directriz"
#
#            try:
#                with connection.cursor() as cursor:
#                    cursor.execute("""
#                        INSERT INTO DIRECTRICES (documento_directriz, nombres_directriz, apellidos_directriz, cargo_directriz, clave_directriz)
#                        VALUES (%s, %s, %s, %s, %s)
#                    """, (documento, nombres, apellidos, cargo, clave))
#                    connection.commit()
#            except Exception as e:
#                return f"Error al guardar en BD: {e}", 500
#
#        # Generar QR
#        json_data = json.dumps(qr_data)
#        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
#        qr.add_data(json_data)
#        qr.make(fit=True)
#        img = qr.make_image(fill_color="black", back_color="white")
#
#        buffer = BytesIO()
#        img.save(buffer, format="PNG")
#        buffer.seek(0)
#        filename = f"{tipo}_{documento}_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
#
#        return send_file(buffer, as_attachment=True, download_name=filename, mimetype='image/png')
#
#    # Obtener datos para mostrar en la tabla
#    try:
#        with connection.cursor(dictionary=True) as cursor:
#            cursor.execute("""
#                    SELECT 
#                        p.documento_persona AS documento, 
#                        CONCAT(p.nombres_persona, ' ', p.apellidos_persona) AS nombre_completo, 
#                        g.grado_grupo AS grado,
#                        p.tipo_personas
#                    FROM PERSONAS p
#                    LEFT JOIN GRADO_GRUPO g ON p.grado_grupo_id = g.id_grado_grado
#                """)
#            estudiantes = cursor.fetchall()
#
#            cursor.execute("""
#                SELECT documento_directriz, 
#                       CONCAT(nombres_directriz, ' ', apellidos_directriz) AS nombre_completo, 
#                       clave_directriz 
#                FROM DIRECTRICES
#            """)
#            directrices = cursor.fetchall()
#    except Exception as e:
#        return f"Error al obtener datos: {e}", 500
#    finally:
#        connection.close()
#
#    return render_template("generador_qr.html", estudiantes=estudiantes, directrices=directrices)
#

import mysql.connector
from flask_cors import CORS
from db import get_connection
from datetime import datetime
from flask import request, render_template, send_file
import qrcode
import json
from io import BytesIO


def generar_qr_pa():
    connection = get_connection()
    estudiantes = []
    directrices = []

    if request.method == 'POST':
        tipo = request.form.get('tipo')
        documento = request.form.get('documento')
        nombres = request.form.get('nombres')
        apellidos = request.form.get('apellidos')

        qr_data = {
            "tipo": tipo,
            "documento": documento,
            "nombres": nombres,
            "apellidos": apellidos
        }

        if tipo == "directriz":
            clave = request.form.get('clave')
            cargo = "directriz"

            try:
                cursor = connection.cursor()
                cursor.execute("""
                    INSERT INTO DIRECTRICES 
                    (documento_directriz, nombres_directriz, apellidos_directriz, cargo_directriz, clave_directriz)
                    VALUES (%s, %s, %s, %s, %s)
                """, (documento, nombres, apellidos, cargo, clave))
                connection.commit()
                cursor.close()
            except Exception as e:
                return f"Error al guardar en BD: {e}", 500

        # Generar QR
        json_data = json.dumps(qr_data)
        qr = qrcode.QRCode(
            version=1, error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10, border=4
        )
        qr.add_data(json_data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
        filename = f"{tipo}_{documento}_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"

        return send_file(buffer, as_attachment=True, download_name=filename, mimetype='image/png')

    # Obtener datos para mostrar en la tabla
    try:
        cursor = connection.cursor(dictionary=True)

        # Estudiantes y egresados
        cursor.execute("""
            SELECT 
                p.documento_persona AS documento, 
                CONCAT(p.nombres_persona, ' ', p.apellidos_persona) AS nombre_completo, 
                COALESCE(g.grado_grupo, 'Egresado') AS grado,
                p.tipo_personas
            FROM PERSONAS p
            LEFT JOIN GRADO_GRUPO g ON p.grado_grupo_id = g.id_grado_grado
        """)
        estudiantes = cursor.fetchall()

        # Directrices
        cursor.execute("""
            SELECT 
                documento_directriz, 
                CONCAT(nombres_directriz, ' ', apellidos_directriz) AS nombre_completo, 
                clave_directriz 
            FROM DIRECTRICES
        """)
        directrices = cursor.fetchall()

        cursor.close()
    except Exception as e:
        return f"Error al obtener datos: {e}", 500
    finally:
        connection.close()

    return render_template("generador_qr.html", estudiantes=estudiantes, directrices=directrices)
