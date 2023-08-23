pipeline {
    agent any
    stages {
        stage('Run API Tests') {
            steps {
                sh 'python3 -m venv env'
                sh '. env/bin/activate'
                sh 'pip install -r requirements.txt'
                sh 'pytest test_api.py'
            }
        }
        stage('Run UI Tests') {
            steps {
                sh 'python3 -m venv env'
                sh '. env/bin/activate'
                sh 'pip install -r requirements.txt'
                sh 'pytest test_ui.py'
        }
        }
        stage('Run DB Tests') {
            steps {
                h 'python3 -m venv env'
                sh '. env/bin/activate'
                sh 'pip install -r requirements.txt'
                sh 'pytest test_db.py'
            }
        }
    }
}
