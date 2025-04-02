
pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/jkbarathkumar/devsecops-sonarqube.git'            
            }
        }
        
        stage('Build') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }
        
        stage('SonarQube Analysis') {
            environment {
                SONARQUBE_URL = 'http://localhost:9000'
                SONARQUBE_TOKEN = credentials('sonarqube-token')
            }
            steps {
                sh '''
                source venv/bin/activate
                sonar-scanner -Dsonar.projectKey=vulnerable-python-project -Dsonar.sources=. -Dsonar.host.url=$SONARQUBE_URL -Dsonar.login=$SONARQUBE_TOKEN
                '''
            }
        }
    }
}
