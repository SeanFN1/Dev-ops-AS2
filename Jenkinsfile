pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                echo 'Installing Python dependencies'
                bat 'pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                echo 'Running pytest'
                bat 'set PYTHONPATH=%CD% && pytest'
            }
        }
    }
}