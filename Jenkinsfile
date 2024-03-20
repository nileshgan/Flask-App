pipeline {
    agent any
    stages {

        stage('Git Checkout') {
            steps {
                git credentialsId: 'github', url: 'https://github.com/nileshgan/Flask-App.git'
            }
        }
         stage('Code Build') {
            steps {
                echo 'Building Flask app...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying Flask app...'
                sh 'python3 /home/ubuntu/python-project/app.py &'
                sh 'sudo systemctl restart nginx'
            }
        }

    }
}

