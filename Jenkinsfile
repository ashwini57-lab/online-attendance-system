pipeline {

    agent any

    stages {

        stage('Clone') {

            steps {
                checkout scm
            }

        }

        stage('Build Docker Image') {

            steps {

                sh 'docker compose build'

            }

        }

        stage('Run Docker Containers') {

            steps {

                sh 'docker compose down || true'

                sh 'docker compose up -d'

            }

        }

        stage('Verify Containers') {

            steps {

                sh 'docker ps'

            }

        }

    }

}