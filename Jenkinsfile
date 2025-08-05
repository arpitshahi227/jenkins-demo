pipeline {
    agent any

    stages {
        stage('Create Virtual Env') {
            steps {
                bat 'python -m venv venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '.\\venv\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '.\\venv\\Scripts\\pytest -v tests\\ --junitxml=report.xml'
            }
        }

        stage('Publish Results') {
            steps {
                junit 'report.xml'
            }
        }
    }
}
