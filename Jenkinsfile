pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building the project...'
                sh 'chmod +x ./build.sh'
                sh './build.sh'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh './run_tests.sh'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                sh './deploy.sh'
            }
        }
    }
}
