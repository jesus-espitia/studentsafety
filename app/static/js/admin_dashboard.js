
fetch('/api/grupos')
    .then(response => response.json())
    .then(data => {
        const select = document.getElementById('grupo_id');
        data.forEach(grupo => {
            const option = document.createElement('option');
            option.value = grupo.id;
            option.textContent = `${grupo.grado} - Dirigido por ${grupo.director}`;
            select.appendChild(option);
        });
    });


function verAsistencias() {
    const grupoId = document.getElementById('grupo_id').value;
    if (!grupoId) {
        document.getElementById('error').textContent = 'Por favor selecciona un grupo.';
        return;
    }

    window.location.href = `/consultar_asistencias?grupo_id=${grupoId}`;
}