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
                sh 'echo ""Testing completed for the python project"'
                sh 'ps -ef'
                sh 'sudo apt udpate'
                }
        }
    }

    post{
        success {
            archiveArtifacts artifacts: 'Build_Python_project/**'
        }
    }
}

