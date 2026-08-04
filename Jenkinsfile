pipeline {

    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'pwd'
                sh 'ls -la'
                sh 'docker compose build'
            }
        }

        stage('Run Containers') {
            steps {
                sh 'docker compose down || true'
                sh 'docker compose up -d'
            }
        }

        stage('Verify') {
            steps {
                sh 'docker ps'
            }
        }
    }
}