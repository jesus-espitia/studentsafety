import cv2
from pyzbar import pyzbar
import json
import tkinter as tk
from PIL import Image, ImageTk
from flask import Blueprint
from app.controllers.acceso import procesar_qr

bp = Blueprint('qr_scanner', __name__)

def iniciar_escaneo():
    cap = cv2.VideoCapture(0)

    root = tk.Tk()
    root.title("Escáner QR - StudentSafety")

    label_video = tk.Label(root)
    label_video.pack()

    def cerrar():
        cap.release()
        root.destroy()

    def escanear():
        ret, frame = cap.read()
        if ret:
            qr_codes = pyzbar.decode(frame)
            for qr in qr_codes:
                qr_data = qr.data.decode('utf-8')
                try:
                    data = json.loads(qr_data)
                    procesar_qr(data)
                except json.JSONDecodeError:
                    print("Código QR no válido")
            # Mostrar en la ventana
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            imgtk = ImageTk.PhotoImage(image=img)
            label_video.imgtk = imgtk
            label_video.configure(image=imgtk)
        root.after(10, escanear)

    btn = tk.Button(root, text="Cerrar", command=cerrar)
    btn.pack()

    escanear()
    root.mainloop()
