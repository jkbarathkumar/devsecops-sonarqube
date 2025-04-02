pipeline {
    agent any

    environment {
        SONARQUBE_SERVER = 'SonarQube'
        SONARQUBE_TOKEN = credentials('sonarqube-token')
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/jkbarathkumar/devsecops-sonarqube.git', branch: 'main'
            }
        }

        stage('Build') {
            steps {
                script {
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withCredentials([string(credentialsId: 'sonarqube-token', variable: 'SONARQUBE_TOKEN')]) {
                    script {
                        sh '''
                            . venv/bin/activate
                            sonar-scanner \
                                -Dsonar.projectKey=devsecops-sonarqube \
                                -Dsonar.sources=. \
                                -Dsonar.host.url=$SONARQUBE_SERVER \
                                -Dsonar.login=$SONARQUBE_TOKEN
                        '''
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
