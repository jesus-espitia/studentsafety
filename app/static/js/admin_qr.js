function onScanSuccess(decodedText, decodedResult) {
            let data;
            try {
                data = JSON.parse(decodedText);
            } catch (e) {
                Swal.fire("QR inválido", "El código escaneado no contiene un JSON válido.", "error");
                return;
            }

            fetch("/verificar_directriz", {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(res => {
                if (res.success) {
                    // Mostrar prompt para clave
                    Swal.fire({
                        title: 'Ingrese su clave',
                        input: 'password',
                        inputPlaceholder: 'Ingrese Clave de Acceso',
                        inputAttributes: { autocapitalize: 'off' },
                        showCancelButton: true,
                        confirmButtonText: 'Acceder',
                        preConfirm: (clave) => {
                            return fetch("/verificar_clave", {
                                method: 'POST',
                                headers: { 'Content-Type': 'application/json' },
                                body: JSON.stringify({ documento: data.documento, clave: clave })
                            })
                            .then(res => res.json())
                            .then(data => {
                                if (!data.success) throw new Error(data.message);
                                return data;
                            })
                            .catch(err => Swal.showValidationMessage(err.message));
                        }
                    }).then(result => {
                        if (result.isConfirmed) {
                            Swal.fire("Acceso permitido", "Bienvenido al área administrativa", "success")
                                .then(() => window.location.href = "/admin_dashboard");
                        }
                    });
                } else {
                    Swal.fire("Acceso denegado", res.message, "error");
                }
            });
        }

        const scanner = new Html5QrcodeScanner("reader", { fps: 10, qrbox: 250 });
        scanner.render(onScanSuccess);