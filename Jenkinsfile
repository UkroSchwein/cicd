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
                // Делаем скрипт build.sh исполнимым
                sh 'chmod +x ./build.sh'
                // Запускаем build.sh
                sh './build.sh'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                // Делаем скрипт run_tests.sh исполнимым
                sh 'chmod +x ./run_tests.sh'
                // Запускаем run_tests.sh
                sh './run_tests.sh'
            }
        }

        stage('Deploy to Staging') {
            steps {
                echo 'Deploying to staging server...'
                // Делаем скрипт deploy.sh исполнимым
                sh 'chmod +x ./deploy.sh'
                // Запускаем deploy.sh для staging
                sh './deploy.sh staging'
            }
        }

        stage('Deploy to Production') {
            when {
                branch 'main'  // Выполняется только на главной ветке
                beforeAgent true
            }
            steps {
                echo 'Deploying to production server...'
                // Делаем скрипт deploy.sh исполнимым
                sh 'chmod +x ./deploy.sh'
                // Запускаем deploy.sh для production
                sh './deploy.sh production'
            }
        }
    }
}
