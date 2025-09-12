from flask import Flask, request, jsonify, render_template
from flask import send_file
import qrcode
import json
from io import BytesIO
from flask import session
from routes import qr_asistencia, admin_qr, verificar_clave, admin_dashboard, asistencias, ver_grupos, generar_qr, documento_excel
import mysql.connector
from flask_cors import CORS
from db import get_connection
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'n8m$gub*(#)/YnhN!(N5t'
CORS(app)
#===================================================================================================
#PAGINA DE INICIO
@app.route('/')
def index():
    return render_template('index.html')

#===================================================================================================
#===================================================================================================
#ESCANER DE ASISTENCIAS
@app.route('/escaner')
def escaner():
    return render_template('qr_asistencia.html')  

@app.route('/registrar_asistencia', methods=['POST'])
def qr_asistencia_interface():
    return qr_asistencia.registrar_asistencia()

#===================================================================================================
#===================================================================================================
# ADMINISTRADOR
@app.route('/admin_qr')
def admin_qrs():
    return render_template('admin_qr.html')

@app.route('/verificar_directriz', methods=['POST'])
def verificar_directriz_interface():
    return admin_qr.verificar_directriz()

#===================================================================================================
#===================================================================================================
#VERIFICACION DE CLAVE
@app.route('/verificar_clave', methods=['POST'])
def verificar_claves():
    return verificar_clave.verificar_clave()

#===================================================================================================
#===================================================================================================
#PANEL DE ADMINISTRADOR
@app.route('/admin_dashboard')
def admin_dashboards():
    return admin_dashboard.admin_dashboard()

#===================================================================================================
#===================================================================================================
#VERIFICAR Y MOSTRAR ASISTENCIA
@app.route('/consultar_asistencias')
def consultar_asistencia():
    return asistencias.consultar_asistencias()

#===================================================================================================
#===================================================================================================
#MOSTRAR GRUPOS
@app.route('/api/grupos')
def api_grupo():
    return ver_grupos.api_grupos()

#===================================================================================================
#===================================================================================================
#GENERADOR DE QR'S
@app.route('/generador_qr', methods=['GET', 'POST'])
def creador_de_qr():
    return generar_qr.generar_qr_pa()

#===================================================================================================
#===================================================================================================
#PÁGINA DE DESCARGA DE EXCEL
@app.route('/reportes_asistencias')
def reportes_asistencias():
    return documento_excel.vista_reportes()

@app.route('/descargar_asistencias', methods=['POST'])
def descargar_asistencia_excel():
    return documento_excel.descargar_asistencias()
#===================================================================================================


if __name__ == '__main__':
    app.run(debug=True)
