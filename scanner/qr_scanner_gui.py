import cv2
import json
from pyzbar.pyzbar import decode
import webbrowser
import mysql.connector

def verificar_admin(documento):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="tu_clave",
        database="qr_scanner_db"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE numero_documento = %s AND tipo = 'admin'", (documento,))
    admin = cursor.fetchone()
    conn.close()
    return admin is not None

def escanear_qr_para_admin():
    cap = cv2.VideoCapture(0)
    print("Escanea un QR de administrador...")

    while True:
        ret, frame = cap.read()
        for qr in decode(frame):
            data = qr.data.decode("utf-8")
            try:
                info = json.loads(data)
                if info.get("tipo") == "admin_access":
                    documento = info.get("documento")
                    if verificar_admin(documento):
                        print("Acceso administrador concedido.")
                        cap.release()
                        cv2.destroyAllWindows()
                        webbrowser.open("http://localhost:5000/dashboard")
                        return
                    else:
                        print("⚠️ Documento no registrado como admin.")
                else:
                    print("⚠️ QR no válido para acceso admin.")
            except json.JSONDecodeError:
                print("⚠️ Formato QR inválido.")
        cv2.imshow("Escáner QR Admin", frame)
        if cv2.waitKey(1) == 27:  # ESC para salir
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    escanear_qr_para_admin()
