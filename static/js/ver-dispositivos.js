// Seleccionar todas las filas que tienen la clase 'clickable-row'
document.querySelectorAll('.clickable-row').forEach(row => {
    row.addEventListener('click', function() {
        // Obtener el valor del atributo data-href y redirigir al enlace
        window.location.href = this.getAttribute('data-href');
    });
});
