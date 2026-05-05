pipeline {

    agent any

    environment {
        IMAGE = "kwamasco/basicmonitoringapp4k8s"
        TAG = "v${BUILD_NUMBER}"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'master',
                url: 'https://github.com/kwamasco23/Pyton-Monitoring-App.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t $IMAGE:$TAG ."
            }
        }

        stage('Push Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    usernameVariable: 'USER',
                    passwordVariable: 'PASS'
                )]) {

                    sh '''
                    echo $PASS | docker login -u $USER --password-stdin
                    docker push $IMAGE:$TAG
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                export KUBECONFIG=/var/lib/jenkins/kubeconfig

                /usr/local/bin/kubectl set image deployment/monitoring-app \
                monitoring-app=$IMAGE:$TAG

                /usr/local/bin/kubectl rollout status deployment/monitoring-app
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Deployment successful: $IMAGE:$TAG"
        }
        failure {
            echo "❌ Pipeline failed"
        }
    }
}
