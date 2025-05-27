import tkinter as tk
from app.controllers.base import get_db
from tkinter import messagebox

def abrir_panel_admin(nombre, apellido):
    root = tk.Tk()
    root.title("Panel Admin - StudentSafety")

    tk.Label(root, text=f"Bienvenido/a {nombre} {apellido}", font=("Arial", 14)).pack(pady=10)

    def mostrar_registros(tabla):
        db = get_db()
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM {tabla}")
        rows = cursor.fetchall()
        top = tk.Toplevel(root)
        top.title(f"Registros - {tabla}")
        text = tk.Text(top, wrap='none')
        for row in rows:
            text.insert(tk.END, str(row) + "\n")
        text.pack(expand=True, fill="both")

    botones = [
        ("Usuarios", lambda: mostrar_registros("usuarios")),
        ("Egresados", lambda: mostrar_registros("egresados")),
        ("Citas", lambda: mostrar_registros("citas")),
        ("Asistencias", lambda: mostrar_registros("asistencias")),
    ]

    for nombre, accion in botones:
        tk.Button(root, text=nombre, width=30, command=accion).pack(pady=5)

    tk.Button(root, text="Cerrar panel", width=30, command=root.destroy).pack(pady=20)

    root.mainloop()
