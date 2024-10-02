pipeline {
    agent any

    environment {
        VENV_DIR = "${WORKSPACE}/venv"
    }

    stages {
        stage('Set up Virtual Environment') {
            steps {
                script {
                    if (!fileExists("${VENV_DIR}/bin/activate")) {
                        sh '''
                            python3 -m venv venv
                            . venv/bin/activate
                            pip install --upgrade pip
                            pip install -r requirements.txt
                        '''
                    } else {
                        echo 'Virtual environment already exists, skipping installation.'
                    }
                }
            }
        }

        stage('Run Tests and Generate Cucumber Report') {
            steps {
                script {
                    sh '''
                        . venv/bin/activate
                        pytest --html=report.html --self-contained-html --cucumber-json=report.json
                    '''
                }
            }
        }

        stage('Publish HTML Report') {
            steps {
                publishHTML([
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: 'Cucumber HTML Report',
                    keepAll: true,
                    alwaysLinkToLastBuild: true,
                    allowMissing: false
                ])
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
