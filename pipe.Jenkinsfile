pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv env'
                sh '. env/bin/activate'
                sh 'pip install -r requirements.txt'
                sh 'export PATH=$PATH:/var/jenkins_home/.local/bin'
            }
        }
        stage('Run API Tests') {
            steps {
                sh 'pytest test_api.py'
            }
        }
        stage('Run UI Tests') {
            steps {
                sh 'pytest test_ui.py'
            }
        }
        stage('Run DB Tests') {
            steps {
                sh 'pytest test_db.py'
            }
        }
    }
}