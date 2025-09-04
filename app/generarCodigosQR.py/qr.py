import qrcode
import json

# Datos en formato JSON
#DIRECTRICES
data = {"cargo":"directriz","documento":"1001", "nombres":"Laura", "apellidos":"Gómez"}
#ESTUDIANTES
data = {"tipo":"estudiante", "documento":"2001", "nombres":"María", "apellidos":"Sánchez"}


# Convertir los datos a una cadena JSON
json_data = json.dumps(data)

# Crear el código QR
qr = qrcode.QRCode(
    version=1,  # controla el tamaño del QR: 1 es el más pequeño
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # nivel de corrección de errores
    box_size=10,  # tamaño de cada "cuadro" del QR
    border=4  # borde en cuadros
)
qr.add_data(json_data)
qr.make(fit=True)

# Generar imagen del QR
img = qr.make_image(fill_color="black", back_color="white")

# Guardar la imagen
img.save("directriz.png")

print("QR generado y guardado como persona_qr.png")
