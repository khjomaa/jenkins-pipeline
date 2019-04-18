pipeline {
    agent any
    stages {
        stage('test') {
            steps {
                dir('.') {
                    sh 'pip install -r requirements.txt'
                    sh 'python3 src/app.py'
                }
            }
        }
    }
    post {
        success {
            dir('.') {
                sh 'python3 src/app.py'
            }
        }
    }
}