pipeline {
    agent any
    stages {
          stage('Install Dependencies') {
            steps {
                script {
                    sh 'python3 -m venv env'
                    sh '. env/bin/activate && pip install -r requirements.txt'
                }
            }
        }
        stage('Run API Tests') {
            steps {
                script {
                    sh '. env/bin/activate'
                    sh 'pytest test_api.py'
                }
            }
        }
        stage('Run UI Tests') {
            steps {
                script {
                    sh '. env/bin/activate'
                    sh 'pytest test_ui.py'
                }
            }
        }
        stage('Run DB Tests') {
            steps {
                script {
                    sh '. env/bin/activate'
                    sh 'pytest test_db.py'
                }
            }
        }
    }
}
