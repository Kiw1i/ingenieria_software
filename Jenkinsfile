pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Kiw1i/ingenieria_software.git'  
            }
        }

        stage('Setup Environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate  # Asegúrate de activar correctamente el entorno virtual
                pip install --upgrade pip
                pip install -r requirements.txt
                pip install pytest-html  # Instalar pytest-html
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                . venv/bin/activate  # Asegúrate de activar el entorno virtual
                pytest test/ --html=report.html --self-contained-html
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts allowEmptyArchive: true, artifacts: 'report.html', onlyIfSuccessful: true
        }
    }
}
