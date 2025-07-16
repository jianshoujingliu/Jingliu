pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/jianshoujingliu/Jingliu.git'
            }
        }
        stage('Build') {
            steps {
                echo 'Building...'
            }
        }
    }
}
