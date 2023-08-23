pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv env'
                sh '. env/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run API Tests') {
            steps {
                bat 'pytest test_api.py'
            }
        }
        stage('Run UI Tests') {
            steps {
                bat 'pytest  test_ui.py'
            }
        }
        stage('Run DB Tests') {
            steps {
                bat 'pytest  test_db.py'
            }
        }
    }
}
