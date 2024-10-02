pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    // Create the virtual environment
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Tests and Generate Reports') {
            steps {
                script {
                    // Ensure the virtual environment is activated before running tests
                    sh '''
                        . venv/bin/activate
                        pytest --html=report.html --self-contained-html --alluredir=allure-results
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

        stage('Publish Allure Results') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'allure-results']]
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
