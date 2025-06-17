pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/yashbc1992/flask-ci-cd.git'
            }
        }

        stage('Build') {
            steps {
                sh """
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                """
            }
        }

        stage('Test') {
            steps {
                sh """
                source venv/bin/activate
                pytest test_app.py
                """
            }
        }

        stage('Deploy') {
            steps {
                sh './deploy.sh'
            }
        }
    }
}
