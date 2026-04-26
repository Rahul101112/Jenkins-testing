pipeline {
    agent any   // Where the pipeline will run

    environment {
        SERVER_IP = "your-server-ip"
        DEPLOY_PATH = "/var/www/html"
    }

    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }

       stage('Deploy') {
            steps {
                withCredentials([
                    string(credentialsId: 'web-server-ip', variable: 'SERVER_IP'),
                    usernamePassword(
                        credentialsId: 'web-server-creds',
                        usernameVariable: 'USER',
                        passwordVariable: 'PASS'
                    )
                ]) {
                    sh '''
                        sshpass -p "$PASS" ssh -o StrictHostKeyChecking=no $USER@$SERVER_IP "ls -ltr
                        hostname
                        whoami
                        pwd
                        ls -lr
                        sudo apt-get update -y
                        "           
                    '''
                }
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