
        function showMessage(msg, type) {
            document.getElementById('result').innerHTML = `<p class="${type}">${msg}</p>`;
        }

        function onScanSuccess(decodedText, decodedResult) {
            let data;
            try {
                data = JSON.parse(decodedText);
            } catch (e) {
                showMessage("El código QR no contiene un JSON válido.", "error");
                return;
            }

            fetch('/registrar_asistencia', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(res => {
                if (res.success) {
                    showMessage(res.message, "ok");
                } else {
                    showMessage(res.message, "error");
                }
            })
            .catch(() => showMessage("Error de conexión con el servidor.", "error"));
        }

        let html5QrcodeScanner = new Html5QrcodeScanner(
            "reader",
            { fps: 10, qrbox: 250 }
        );
        html5QrcodeScanner.render(onScanSuccess);