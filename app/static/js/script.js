
function onScanSuccess(decodedText, decodedResult) {
    let data;
    try {
        data = JSON.parse(decodedText);
    } catch (e) {
        Swal.fire({
            title: "Código inválido",
            text: "El código QR no tiene información válida.",
            icon: "error"
        });
        return;
    }

    Swal.fire({
        title: 'Procesando...',
        text: 'Por favor espera',
        allowOutsideClick: false,
        didOpen: () => {
            Swal.showLoading()
        }
    });

    fetch('/registrar_asistencia', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })
        .then(response => response.json())
        .then(res => {
            Swal.close(); // Cierra el loading

            if (res.success) {
                Swal.fire({
                    title: "¡Éxito!",
                    text: res.message,
                    icon: "success",
                    timer: 3000,
                    showConfirmButton: false
                });
            } else {
                Swal.fire({
                    title: "Atención",
                    text: res.message,
                    icon: "error",
                    timer: 3000,
                    showConfirmButton: false
                });
            }
        })
        .catch(() => {
            Swal.close();
            Swal.fire({
                title: "Error",
                text: "Error de conexión con el servidor.",
                icon: "error",
                timer: 3000,
                showConfirmButton: false
            });
        });
}

let html5QrcodeScanner = new Html5QrcodeScanner(
    "reader",
    { fps: 10, qrbox: 250 }
);
html5QrcodeScanner.render(onScanSuccess);

