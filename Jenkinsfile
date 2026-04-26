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
        emailext(
            to: 'nahipata2022@gmail.com',
            subject: "🚀 Deployment: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
            mimeType: 'text/html',
            body: """
            <html>
            <body style="font-family: Arial;">

                <h2 style="color: #2E86C1;">🚀 Jenkins Deployment Notification</h2>

                <p><b>Status:</b> 
                    <span style="color: ${currentBuild.currentResult == 'SUCCESS' ? 'green' : 'red'};">
                        ${currentBuild.currentResult}
                    </span>
                </p>

                <hr>

                <h3>📦 Build Details</h3>
                <ul>
                    <li><b>Job Name:</b> ${env.JOB_NAME}</li>
                    <li><b>Build Number:</b> ${env.BUILD_NUMBER}</li>
                    <li><b>Build URL:</b> <a href="${env.BUILD_URL}">Open Build</a></li>
                </ul>

                <h3>🐳 Docker Info</h3>
                <ul>
                    <li><b>Image:</b> ${env.IMAGE_NAME}</li>
                    <li><b>Tag:</b> ${env.BUILD_NUMBER}</li>
                </ul>

                <h3>🌐 Application</h3>
                <p>
                    Access your app here:<br>
                    👉 <a href="http://YOUR-SERVER-IP:8081">http://YOUR-SERVER-IP:8081</a>
                </p>

                <hr>

                <p style="color: gray;">
                    This is an automated email from Jenkins CI/CD Pipeline.
                </p>

            </body>
            </html>
            """
        )

        }
        success {
            echo 'Image pushed successfully 🚀'
        }
        failure {
            echo 'Pipeline Failed ❌'
        }
    }
}
