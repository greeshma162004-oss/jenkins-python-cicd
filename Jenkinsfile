pipeline {
    agent any

    environment {
        APP_NAME = 'jenkins-python-cicd'
        VERSION = '1.0'
    }

    parameters {
        choice(
            name: 'ENVIRONMENT',
            choices: ['DEV', 'TEST', 'PROD'],
            description: 'Select the deployment environment'
        )
    }

    stages {

        stage('Build') {
            steps {
                echo 'Building the Python application...'
            }
        }

        stage('Show Environment') {
            steps {
                echo "Application: ${env.APP_NAME}"
                echo "Version: ${env.VERSION}"
                echo "Selected environment: ${params.ENVIRONMENT}"
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

        stage('Tests') {
            parallel {

                stage('Unit Tests') {
                    steps {
                        echo 'Running unit tests...'
                        sh 'venv/bin/pytest'
                    }
                }

        stage('Application Check') {
            steps {
                echo 'Checking application...'
                sh 'venv/bin/python app.py'
            }
        }
    }
}
        stage('Deploy to DEV') {
            when {
                expression {
                    params.ENVIRONMENT == 'DEV'
                }
            }
            steps {
                echo 'Deploying application to DEV...'
            }
        }

        stage('Deploy to TEST') {
            when {
                expression {
                    params.ENVIRONMENT == 'TEST'
                }
            }
            steps {
                echo 'Deploying application to TEST...'
            }
        }

        stage('Deploy to PROD') {
            when {
                expression {
                    params.ENVIRONMENT == 'PROD'
                }
            }
            steps {
                echo 'Deploying application to PROD...'
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
