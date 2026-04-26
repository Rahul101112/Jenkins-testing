pipeline {
    agent any   // Where the pipeline will run

    environment {
        NAME = "Rahul"   // Environment variables
    }

    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Build') {
            steps {
                echo "Building..."
            }
        }

        stage('Test') {
            steps {
                echo "Testing..."
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying..."
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished'
        }
        success {
            echo 'Success!'
        }
        failure {
            echo 'Failed!'
        }
    }
}