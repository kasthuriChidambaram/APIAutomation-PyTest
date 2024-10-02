pipeline {
    agent any

    stages {
        stage('Run Tests and Generate Reports') {
            steps {
                script {
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
                    allowMissing: false  // Added required parameter
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
