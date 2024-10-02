pipeline {
    agent any

    environment {
        VENV_DIR = "${WORKSPACE}/venv"
    }

    stages {
        stage('Set up Virtual Environment') {
            steps {
                script {
                    // Check if the virtual environment already exists
                    if (!fileExists("${VENV_DIR}/bin/activate")) {
                        // Create the virtual environment and install dependencies if not present
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

        stage('Run Tests and Generate HTML Report') {
            steps {
                script {
                    // Activate the virtual environment and run tests
                    sh '''
                        . venv/bin/activate
                        pytest --html=report.html --self-contained-html
                    '''
                }
            }
        }

        stage('Publish HTML Report') {
            steps {
                publishHTML([
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: 'Pytest HTML Report',
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
