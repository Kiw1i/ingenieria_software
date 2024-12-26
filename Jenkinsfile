pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Clonar el repositorio
                git 'https://github.com/Kiw1i/ingenieria_software.git'  // Reemplaza con la URL de tu repositorio
            }
        }

        stage('Setup Environment') {
            steps {
                // Configurar el entorno virtual e instalar dependencias
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                // Ejecutar pruebas unitarias
                sh '''
                source venv/bin/activate
                pytest test/ --junitxml=results.xml
                '''
            }
        }
    }

    post {
        always {
            // Publicar resultados de pruebas
            junit 'results.xml'
        }
    }
}
