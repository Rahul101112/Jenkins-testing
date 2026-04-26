pipeline {
    agent any   // Where the pipeline will run

    environment {
        SERVER_IP = "your-server-ip"
        DEPLOY_PATH = "/var/www/html"
    }

    stages {

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
                        sshpass -p "$PASS" ssh -o StrictHostKeyChecking=no $USER@$SERVER_IP "
                        echo "From SSH session"
                        sudo rm -rf /var/www/html/*
                        sshpass -p "$PASS" scp Jenkinspicto.html $USER@$SERVER_IP:/var/www/html/index.html
                        sudo systemctl reload nginx                        
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