pipeline {
    agent any
    environment {
        PATH = "/usr/local/bin:$PATH"
    }
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
                sh 'pytest test_api.py'
            }
        }
        stage('Run UI Tests') {
            steps {
                sh 'xvfb-run pytest test_ui.py'
            }
        }
        stage('Run DB Tests') {
            steps {
                sh 'pytest test_db.py'
            }
        }
    }
}
