pipeline {
    agent {
        src/mypackage
    }
    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        stage('point') {
            steps {
                echo 'point'
                sh 'pwd'
                sh 'ls'
                sh 'cd src'
                sh 'pwd'
                sh 'cd mypackage'
            }
        }
        stage('build') {
            steps {
                echo 'build'
                sh 'python3 job.py'
            }
        }
    }
}