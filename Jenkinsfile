pipeline {
    agent any

    tools {
        python 'Python310' // Jenkins Global Tool Config me set hona chahiye
    }

    stages {
        stage('Clone Repo') {
            steps {
                // Git automatically pulls if SCM configured, so optional
                echo 'Code pulled from GitHub'
            }
        }

        stage('Create Virtual Env & Install Deps') {
            steps {
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    call venv\\Scripts\\activate
                    pytest --maxfail=1 --disable-warnings --html=report.html
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
            junit '**/test-results/*.xml' // if pytest junitxml used
            cleanWs()
        }
    }
}
