pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/UstinskiyRoman/Laba11'
            }
        }

        stage('Install Requirements') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh 'python -m unittest discover -s . -p "Tests.py" > results.xml'
                }
            }
        }
    }
}