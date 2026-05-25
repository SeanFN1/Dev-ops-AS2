pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                echo 'Installing Python dependencies'
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                echo 'Running pytest'
                bat 'set PYTHONPATH=%CD% && python -m pytest'
            }
        }
    }
}