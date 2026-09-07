pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building the Python application...'
            }
        }

        stage('Test') {
            steps {
                echo 'Running automated tests...'
                sh 'pytest'
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