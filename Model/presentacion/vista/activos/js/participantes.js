// Archivo: presentacion/vista/activos/js/participantes.js

document.addEventListener('DOMContentLoaded', () => {
    const listaParticipantes = document.getElementById('lista-participantes');
    const form = document.getElementById('form-participante');

    // Función para obtener y mostrar la lista de participantes
    const cargarParticipantes = () => {
        fetch('/participantes')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Error al cargar los participantes');
                }
                return response.json();
            })
            .then(data => {
                mostrarParticipantes(data);
            })
            .catch(error => {
                console.error('Error:', error);
                mostrarError('No se pudieron cargar los participantes.');
            });
    };

    // Función para mostrar los participantes en la lista
    const mostrarParticipantes = (participantes) => {
        listaParticipantes.innerHTML = ''; // Limpiar la lista antes de agregar los nuevos participantes
        participantes.forEach(participante => {
            const item = document.createElement('li');
            item.textContent = participante.nombre;
            listaParticipantes.appendChild(item);
        });
    };

    // Función para manejar el envío del formulario y agregar un nuevo participante
    const agregarParticipante = (event) => {
        event.preventDefault();
        const nombre = document.getElementById('nombre').value;

        fetch('/participantes', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ nombre: nombre })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Error al agregar el participante');
            }
            return response.json();
        })
        .then(participante => {
            const item = document.createElement('li');
            item.textContent = participante.nombre;
            listaParticipantes.appendChild(item);
            form.reset(); // Limpiar el formulario después de agregar el participante
        })
        .catch(error => {
            console.error('Error:', error);
            mostrarError('No se pudo agregar el participante.');
        });
    };

    // Función para mostrar errores en la consola
    const mostrarError = (mensaje) => {
        console.error(mensaje);
    };

    // Eventos
    form.addEventListener('submit', agregarParticipante);
    cargarParticipantes(); // Cargar participantes al cargar la página
});
