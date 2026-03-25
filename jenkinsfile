pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
            }
        }

        stage('Run') {
            steps {
                sh 'python3 web2.py'
            }
        }
    }
}
