pipeline {
    agent any
    stages {
          stage('Install Dependencies') {
            steps {
                script {
                    sh 'python3 -m venv env'
                    sh '. env/bin/activate && pip install -r requirements.txt'
                    sh 'deactivate'
                }
            }
        }
        stage('Run API Tests') {
            steps {
                script {
                    sh '. env/bin/activate'
                    sh 'pip install pytest'
                    sh 'pytest test_api.py'
                    sh 'deactivate'
                }
            }
        }
        stage('Run UI Tests') {
            steps {
                script {
                    sh '. env/bin/activate'
                    sh 'pip install pytest'
                    sh 'pytest test_ui.py'
                    sh 'deactivate'
                }
            }
        }
        stage('Run DB Tests') {
            steps {
                script {
                    sh '. env/bin/activate'
                    sh 'pip install pytest'
                    sh 'pytest test_db.py'
                    sh 'deactivate'
                }
            }
        }
    }
}
