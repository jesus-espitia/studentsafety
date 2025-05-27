from app.controllers.base import get_db
from datetime import datetime
import tkinter.messagebox as msgbox

def procesar_qr(data):
    tipo = data.get("tipo")
    documento = data.get("documento")

    if not tipo or not documento:
        msgbox.showerror("Error", "El código QR no contiene la información necesaria.")
        return

    if tipo == "admin_access":
        mostrar_panel_admin(documento)
    elif tipo in ("estudiante", "profesor"):
        registrar_asistencia(documento, tipo)
    elif tipo == "egresado":
        validar_cita_egresado(documento)
    else:
        msgbox.showerror("Tipo no válido", f"Tipo '{tipo}' no reconocido.")

def registrar_asistencia(documento, tipo_usuario):
    db = get_db()
    cursor = db.cursor()

    # Verificar existencia en tabla usuarios
    cursor.execute("SELECT nombre, apellido FROM usuarios WHERE numero_documento = %s AND tipo = %s", (documento, tipo_usuario))
    result = cursor.fetchone()
    
    if result:
        cursor.execute("INSERT INTO asistencias (documento_usuario, tipo_usuario) VALUES (%s, %s)", (documento, tipo_usuario))
        db.commit()
        nombre = f"{result[0]} {result[1]}"
        msgbox.showinfo("Ingreso autorizado", f"{nombre} ({tipo_usuario}) ha sido registrado.")
    else:
        msgbox.showerror("Denegado", f"No se encontró un {tipo_usuario} con documento {documento}.")

def validar_cita_egresado(documento):
    db = get_db()
    cursor = db.cursor()

    # Verificar si existe el egresado
    cursor.execute("SELECT nombre, apellido FROM egresados WHERE numero_documento = %s", (documento,))
    egresado = cursor.fetchone()

    if not egresado:
        msgbox.showerror("Denegado", "Egresado no registrado.")
        return

    # Verificar cita confirmada para hoy
    ahora = datetime.now()
    cursor.execute("""
        SELECT fecha_cita FROM citas 
        WHERE documento_egresado = %s 
        AND estado = 'confirmada' 
        AND DATE(fecha_cita) = CURDATE()
    """, (documento,))
    cita = cursor.fetchone()

    if cita:
        cursor.execute("INSERT INTO asistencias (documento_usuario, tipo_usuario) VALUES (%s, %s)", (documento, 'egresado'))
        db.commit()
        nombre = f"{egresado[0]} {egresado[1]}"
        msgbox.showinfo("Ingreso autorizado", f"{nombre} ha ingresado con cita.")
    else:
        msgbox.showerror("Sin cita", "Este egresado no tiene cita confirmada para hoy.")

def mostrar_panel_admin(documento):
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT nombre, apellido FROM usuarios WHERE numero_documento = %s AND tipo = 'admin'", (documento,))
    admin = cursor.fetchone()

    if admin:
        from app.views.admin_gui import abrir_panel_admin
        abrir_panel_admin(nombre=admin[0], apellido=admin[1])
    else:
        msgbox.showerror("Acceso denegado", "Este usuario no tiene permisos de administrador.")
