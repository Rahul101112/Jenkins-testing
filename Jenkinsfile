pipeline {
    agent any

    stages {

        stage('Build_Python_project') 
        {
            steps {
                sh 'python3 web2.py'
                }
        }

        stage('Test_python') 
        {
            steps {
                sh 'echo "Testing completed for the python project"'
                sh 'ps -ef'
                sh 'ip addr >> new.txt'
                sh 'cat new.txt'
                }
        }
    }

    post{
        success {
            
            sh 'ls -lh'
            archiveArtifacts artifacts: 'Jenkins-testing/**'
        }
    }
}

