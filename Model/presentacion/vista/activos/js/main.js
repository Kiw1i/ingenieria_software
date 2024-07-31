// Archivo: presentacion/vista/activos/js/main.js

// Módulo para manejar el comportamiento de los participantes
const ParticipantesModule = (() => {

    // Inicialización del módulo
    const init = () => {
        document.addEventListener('DOMContentLoaded', () => {
            console.log("Documento cargado y listo."); // Log para indicar que el documento está completamente cargado
            cargarParticipantes(); // Cargar participantes al cargar la página
        });
    };

    // Función para cargar los participantes
    const cargarParticipantes = () => {
        fetch('/api/participantes')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Error al cargar los participantes');
                }
                return response.json();
            })
            .then(data => {
                console.log(data); // Log de los participantes cargados
                mostrarParticipantes(data); // Mostrar participantes en la interfaz
            })
            .catch(error => {
                console.error('Error:', error); // Log de cualquier error al cargar los participantes
                mostrarError('No se pudieron cargar los participantes.');
            });
    };

    // Función para mostrar los participantes en la interfaz
    const mostrarParticipantes = (participantes) => {
        const listaParticipantes = document.getElementById('lista-participantes');
        listaParticipantes.innerHTML = ''; // Limpiar la lista antes de agregar los nuevos participantes

        participantes.forEach(participante => {
            const li = document.createElement('li');
            li.textContent = participante.nombre;
            listaParticipantes.appendChild(li);
        });
    };

    // Función para mostrar un error en la interfaz
    const mostrarError = (mensaje) => {
        const errorContainer = document.getElementById('error-container');
        if (errorContainer) {
            errorContainer.textContent = mensaje;
            errorContainer.style.display = 'block';
        } else {
            console.error('No se encontró el contenedor de errores.');
        }
    };

    // Retornar las funciones públicas del módulo
    return {
        init,
    };

})();

// Inicializar el módulo
ParticipantesModule.init();

