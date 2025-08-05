pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Setup Virtualenv & Install Dependencies') {
            steps {
                bat '''
                    python -m venv %VENV_DIR%
                    call %VENV_DIR%\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Pytest') {
            steps {
                bat '''
                    call %VENV_DIR%\\Scripts\\activate
                    pytest --maxfail=1 --disable-warnings --html=report.html
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
            cleanWs()
        }
    }
}
