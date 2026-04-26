pipeline {
    agent any

     environment {
        ACR_NAME = "jenkinstesting1801.azurecr.io"
        ACR_LOGIN = "jenkinstesting1801"
        IMAGE_NAME = "myapp"
        TAG = "${env.BUILD_NUMBER}"
    }

    stages {
        stage('Check Agent') {
            steps {
                echo "Running on node: ${env.NODE_NAME}"
                echo "Workspace: ${env.WORKSPACE}"
                sh 'whoami'
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

        stage('Build Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$TAG .'
            }
        }

        stage('Tag Image') {
            steps {
                sh 'docker tag $IMAGE_NAME:$TAG $ACR_URL/$IMAGE_NAME:$TAG'
            }
        }

        stage('Login to ACR') {
            steps {
                withCredentials([azureServicePrincipal(
                    credentialsId: 'jenkins_SP',   // <-- your Jenkins credential ID
                    clientIdVariable: 'AZ_CLIENT_ID',
                    clientSecretVariable: 'AZ_CLIENT_SECRET'
                )]) {
                    sh '''
                        echo $AZ_CLIENT_SECRET | docker login $ACR_URL \
                        -u $AZ_CLIENT_ID --password-stdin
                    '''
                }
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push $ACR_URL/$IMAGE_NAME:$TAG'
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
