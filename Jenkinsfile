pipeline {
    agent any

    environment {
        ACR_NAME = 'jenkinstesting1801.azurecr.io'
        IMAGE_NAME = 'myapp'
        TAG = "${env.BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
    steps {
        checkout scm
    }
}
        stage('Check Agent') {
            steps {
                // echo "Running on node: ${env.NODE_NAME}"
                // echo "Workspace: ${env.WORKSPACE}"
                sh 'whoami'
                sh 'hostname'
            }
        }

        stage('Deploy to Nginx') {
            steps {
                withCredentials([
                string(credentialsId: 'web-server-ip', variable: 'SERVER_IP'),
                usernamePassword(
                credentialsId: 'web-server-creds',
                usernameVariable: 'USER',
                passwordVariable: 'PASS'
                        )
                ]) 
                
                {
                    sh '''
                echo "Cleaning Nginx web directory..."

                sshpass -p "$PASS" ssh -o StrictHostKeyChecking=no $USER@$SERVER_IP "
                    sudo rm -rf /usr/share/nginx/html/*
                "

                echo "Copying snake.html..."

                sshpass -p "$PASS" scp -o StrictHostKeyChecking=no \
                    snake.html \
                    $USER@$SERVER_IP:/usr/share/nginx/html/index.html

                echo "Reloading Nginx..."

                sshpass -p "$PASS" ssh -o StrictHostKeyChecking=no $USER@$SERVER_IP "
                    sudo systemctl reload nginx
                "
                '''
                }
            }
        }

        // stage('Build Image') {
        //     steps {
        //         echo "Running on node: ${env.NODE_NAME}"
        //         echo "Workspace: ${env.WORKSPACE}"
        //         sh '''
        //         docker build -t $IMAGE_NAME:$TAG .
        //         docker tag $IMAGE_NAME:$TAG $ACR_NAME/$IMAGE_NAME:$TAG
        //         '''
        //     }
        // }

        // stage('SonarQube Analysis') {
        //     steps {
        //         withSonarQubeEnv('SonarQube') {
        //             withCredentials([string(credentialsId: 'SoranQubeToken', variable: 'SONAR_TOKEN')]) {
        //                 sh '''
        //             /opt/sonar-scanner/bin/sonar-scanner -v
        //             echo "===== RUNNING SCAN ====="

        //             /opt/sonar-scanner/bin/sonar-scanner \
        //             -Dsonar.projectKey=myapp \
        //             -Dsonar.sources=. \
        //             -Dsonar.host.url=$SONAR_HOST_URL \
        //             -Dsonar.login=$SONAR_TOKEN

        //             echo "===== AFTER SCAN ====="
        //             ls -l
        //         '''
        //             }
        //         }
        //     }
        // }

        // stage('Quality Gate') {
        //     steps {
        //         timeout(time: 2, unit: 'MINUTES') {
        //             waitForQualityGate abortPipeline: true
        //         }
        //     }
        // }

        // stage('Login to ACR') {
        //     steps {
        //         withCredentials([azureServicePrincipal(
        //             credentialsId: 'jenkins_SP',
        //             clientIdVariable: 'AZ_CLIENT_ID',
        //             clientSecretVariable: 'AZ_CLIENT_SECRET'
        //         )]) {
        //             sh '''
        //                 echo $AZ_CLIENT_SECRET | docker login $ACR_NAME \
        //                 -u $AZ_CLIENT_ID --password-stdin
        //             '''
        //         }
        //     }
        // }

        // stage('Push Image') {
        //     steps {
        //         sh 'docker push $ACR_NAME/$IMAGE_NAME:$TAG'
        //     }
        // }

        // // 🔥 Optional: also tag latest
        // stage('Tag & Push Latest') {
        //     steps {
        //         sh '''
        //             docker tag $IMAGE_NAME:$TAG $ACR_NAME/$IMAGE_NAME:latest
        //             docker push $ACR_NAME/$IMAGE_NAME:latest
        //         '''
        //     }
        // }

        // stage('Deploy to VM') {
        //     steps {
        //         withCredentials([
        //             string(credentialsId: 'web-server-ip', variable: 'SERVER_IP'),
        //             usernamePassword(
        //                 credentialsId: 'web-server-creds',
        //                 usernameVariable: 'USER',
        //                 passwordVariable: 'PASS'
        //             ),
        //             azureServicePrincipal(
        //                 credentialsId: 'jenkins_SP',
        //                 clientIdVariable: 'AZ_CLIENT_ID',
        //                 clientSecretVariable: 'AZ_CLIENT_SECRET'
        //             )
        //         ]) {
        //             sh """
        //                 sshpass -p "$PASS" ssh -o StrictHostKeyChecking=no $USER@$SERVER_IP \\
        //                 "echo $AZ_CLIENT_SECRET | docker login $ACR_NAME \\
        //                 -u $AZ_CLIENT_ID --password-stdin && \\
        //                 docker stop myapp || true && \\
        //                 docker rm myapp || true && \\
        //                 docker pull $ACR_NAME/$IMAGE_NAME:latest && \\
        //                 docker run -d -p 8081:80 --name myapp $ACR_NAME/$IMAGE_NAME:latest"
        //             """
        //         }
        //     }
        // }
    }

    post {
        // always {
        //     emailext(
        //         to: 'nahipata2022@gmail.com',
        //         subject: "Build ${currentBuild.currentResult}: ${env.JOB_NAME}",
        //         body: "Check: ${env.BUILD_URL}"
        //     )
        // }
        success {
            echo 'Image pushed successfully 🚀'
        }
        failure {
            echo 'Pipeline Failed ❌'
        }
    }
}
