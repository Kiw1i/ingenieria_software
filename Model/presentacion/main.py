# Archivo: main.py

from presentacion import create_app

def main():
    """
    Punto de entrada principal para ejecutar la aplicación Flask.
    """
    # Crear una instancia de la aplicación Flask
    app = create_app()

    # Ejecutar la aplicación en modo de depuración
    app.run(debug=True)

if __name__ == "__main__":
    main()
