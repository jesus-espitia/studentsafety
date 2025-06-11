function toggleClave() {
    const tipo = document.getElementById('tipo').value;
    const claveGroup = document.getElementById('clave-group');
    claveGroup.style.display = tipo === 'directriz' ? 'block' : 'none';
}

function toggleTable() {
    const tipo = document.getElementById('tabla_tipo').value;
    document.getElementById('tabla_estudiantes').style.display = tipo === 'estudiantes' ? 'table' : 'none';
    document.getElementById('tabla_directrices').style.display = tipo === 'directrices' ? 'table' : 'none';
}

document.addEventListener('DOMContentLoaded', () => {
    toggleClave();
    toggleTable();
});