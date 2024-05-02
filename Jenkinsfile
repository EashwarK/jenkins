pipeline {
    agent { 
        node {
            label 'docker-agent-python'
        }
    }
    triggers {
        pollSCM '* * * * *'
    }
    stages {
        stage('Build') {
            steps {
                echo "Building Folder.."
                sh '''
                echo "Starting the Build and jenkins..."
                '''
            }
        }
        stage('Install') {
            steps {
                echo "Installing requirements.."
                sh '''
                cd myapp
                pip install -r requirements.txt
                '''
            }
        }
        stage('Run') {
            steps {
                echo "Running.."
                sh '''
                cd myapp
                pip install fire
                python3 hello.py
                python3 hello.py --name=Eash
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh '''
                echo "doing deployment stuff.."
                '''
            }
        }
        stage('Notify') {
            steps {
                echo 'Notifying....'
                sh '''
                echo "sending notifications..It is Done"
                '''
            }
        }
    }
    post {
        success {
            echo 'Pipeline succeeded!'
            echo 'Sending success notification...'
        }
        failure {
            echo 'Pipeline failed!'
            echo 'Sending failure notification...'
        }
    }
}
