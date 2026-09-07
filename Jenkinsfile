pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building the Python application...'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Creating Python virtual environment...'
                sh 'python3 -m venv venv'

                echo 'Installing Python dependencies...'
                sh 'venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running automated tests...'
                sh 'venv/bin/pytest'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed!'
        }

        always {
            echo 'Pipeline execution completed.'
        }
    }
}