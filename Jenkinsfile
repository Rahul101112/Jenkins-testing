pipeline {
    agent any

    environment {
        ACR_NAME = 'jenkinstesting1801.azurecr.io'
        IMAGE_NAME = 'myapp'
        TAG = "${env.BUILD_NUMBER}"
    }

    stages {
        // stage('Check Agent') {
        //     steps {
        //         echo "Running on node: ${env.NODE_NAME}"
        //         echo "Workspace: ${env.WORKSPACE}"
        //         sh 'whoami'
        //         sh 'hostname'
        //     }
        // }

        // 🔹 OPTIONAL (Traditional deployment - you can remove later)
        // stage('Deploy to Nginx (Optional)') {
        //     steps {
        //         withCredentials([
        //             string(credentialsId: 'web-server-ip', variable: 'SERVER_IP'),
        //             usernamePassword(
        //                 credentialsId: 'web-server-creds',
        //                 usernameVariable: 'USER',
        //                 passwordVariable: 'PASS'
        //             )
        //         ]) {
        //             sh '''
        //                 echo "Cleaning server..."
        //                 sshpass -p "$PASS" ssh -o StrictHostKeyChecking=no $USER@$SERVER_IP "
        //                     sudo rm -rf /var/www/html/*
        //                 "

        //                 echo "Copying file..."
        //                 sshpass -p "$PASS" scp -o StrictHostKeyChecking=no Jenkinstopic.html $USER@$SERVER_IP:/var/www/html/index.html

        //                 echo "Reloading nginx..."
        //                 sshpass -p "$PASS" ssh -o StrictHostKeyChecking=no $USER@$SERVER_IP "
        //                     sudo systemctl reload nginx
        //                 "
        //             '''
        //         }
        //     }
        // }

        stage('Build Image') {
            steps {
                echo "Running on node: ${env.NODE_NAME}"
                echo "Workspace: ${env.WORKSPACE}"
                sh '''
                docker build -t $IMAGE_NAME:$TAG .
                docker tag $IMAGE_NAME:$TAG $ACR_NAME/$IMAGE_NAME:$TAG

                '''
            }
        }

        stage('Login to ACR') {
            steps {
                withCredentials([azureServicePrincipal(
                    credentialsId: 'jenkins_SP',
                    clientIdVariable: 'AZ_CLIENT_ID',
                    clientSecretVariable: 'AZ_CLIENT_SECRET'
                )]) {
                    sh '''
                        echo $AZ_CLIENT_SECRET | docker login $ACR_NAME \
                        -u $AZ_CLIENT_ID --password-stdin
                    '''
                }
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push $ACR_NAME/$IMAGE_NAME:$TAG'
            }
        }

        // 🔥 Optional: also tag latest
        stage('Tag & Push Latest') {
            steps {
                sh '''
                    docker tag $IMAGE_NAME:$TAG $ACR_NAME/$IMAGE_NAME:latest
                    docker push $ACR_NAME/$IMAGE_NAME:latest
                '''
            }
        }

        stage('Deploy to VM') {
            steps {
                withCredentials([
            string(credentialsId: 'web-server-ip', variable: 'SERVER_IP'),
            usernamePassword(
                credentialsId: 'web-server-creds',
                usernameVariable: 'USER',
                passwordVariable: 'PASS'
            ),
            azureServicePrincipal(
                credentialsId: 'jenkins_SP',
                clientIdVariable: 'AZ_CLIENT_ID',
                clientSecretVariable: 'AZ_CLIENT_SECRET'
            )
        ]) {
                    sh """
                        sshpass -p "$PASS" ssh -o StrictHostKeyChecking=no $USER@$SERVER_IP \\
                        "echo $AZ_CLIENT_SECRET | docker login jenkinstesting1801.azurecr.io \\
                        -u $AZ_CLIENT_ID --password-stdin && \\
                        docker stop myapp || true && \\
                        docker rm myapp || true && \\
                        docker pull jenkinstesting1801.azurecr.io/myapp:latest && \\
                        docker run -d -p 8081:80 --name myapp jenkinstesting1801.azurecr.io/myapp:latest"
                    """
        }
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '*.html', fingerprint: true
        }
        success {
            echo 'Image pushed successfully 🚀'
        }
        failure {
            echo 'Pipeline Failed ❌'
        }
    }
}
