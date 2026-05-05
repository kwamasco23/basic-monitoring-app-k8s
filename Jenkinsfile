pipeline {

    agent any

    environment {
        IMAGE = "kwamasco/basicmonitoringapp4k8s"
        TAG = "v${BUILD_NUMBER}"
        KUBECONFIG = "/var/lib/jenkins/kubeconfig"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'master',
                url: 'https://github.com/kwamasco23/basic-monitoring-app-k8s.git'
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

        stage('Apply Kubernetes Config') {
            steps {
                sh '''
                export KUBECONFIG=$KUBECONFIG
                kubectl apply -f deployment.yaml
                kubectl apply -f service.yaml
                '''
            }
        }

        stage('Update Image') {
            steps {
                sh '''
                export KUBECONFIG=$KUBECONFIG

                kubectl set image deployment/monitoring-app \
                monitoring-app=$IMAGE:$TAG
                '''
            }
        }

        stage('Verify Rollout') {
            steps {
                sh '''
                export KUBECONFIG=$KUBECONFIG
                kubectl rollout status deployment/monitoring-app
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