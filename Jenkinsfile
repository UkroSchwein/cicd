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
                sh 'chmod +x ./run_tests.sh'
                sh './run_tests.sh'
            }
        }

        stage('Deploy to Staging') {
            steps {
                echo 'Deploying to staging server...'
                sh 'chmod +x ./deploy.sh'
                sh './deploy.sh staging'
            }
        }

        stage('Deploy to Production') {
            when {
                branch '*/main'  // Выполняется только на главной ветке
                beforeAgent true
            }
            steps {
                echo 'Deploying to production server...'
                sh 'chmod +x ./deploy.sh'
                sh './deploy.sh production'
            }
        }
    }
}
