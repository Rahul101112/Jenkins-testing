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
                sh 'ip addr > Artifacts/Artifacts.txt'
                }
        }
    }

    post{
        success {
            
            sh 'ls -lh'
            archiveArtifacts artifacts: 'Artifacts/*.txt'
            cleanWs()
        }
    }
}

