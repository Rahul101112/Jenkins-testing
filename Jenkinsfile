pipeline {
    agent any

    environment {
        SERVER_IP = 'your-server-ip'
        DEPLOY_PATH = '/var/www/html'
    }

    stages {
        stage('Check Agent') {
            steps {
                echo "Running on node: ${env.NODE_NAME}"
                echo "Workspace: ${env.WORKSPACE}"
                sh 'hostname'
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
                        echo "Cleaning server..."

                        sshpass -p "$PASS" ssh -o StrictHostKeyChecking=no $USER@$SERVER_IP "
                            sudo rm -rf /var/www/html/*
                        "

                        echo "Copying file..."

                        sshpass -p "$PASS" scp -o StrictHostKeyChecking=no Jenkinstopic.html $USER@$SERVER_IP:/var/www/html/index.html

                        echo "Reloading nginx..."

                        sshpass -p "$PASS" ssh -o StrictHostKeyChecking=no $USER@$SERVER_IP "
                            sudo systemctl reload nginx
                        "
                    '''
                }
            }
        }

        stage('Build') {
            steps {
                echo 'Building...'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing...'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '*.html', fingerprint: true
        }
        success {
            echo 'Success!'
        }
        failure {
            echo 'Failed!'
        }
    }
}
