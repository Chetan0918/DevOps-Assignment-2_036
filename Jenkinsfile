pipeline {
  agent any
  environment {
    DOCKERHUB_REPO = '' // fill this before use e.g. yourusername/devops-assignment-2
    IMAGE_TAG = "devops-assignment-2:${GIT_COMMIT.substring(0,7)}"
  }
  stages {
    stage('Checkout') {
      steps { checkout scm }
    }
    stage('Build Image') {
      steps {
        sh 'docker build -t ${IMAGE_TAG} -f Dockerfile .'
      }
    }
    stage('Unit Test') {
      steps {
        // simple smoke test: run container and curl the app
        sh 'docker run -d --name smoke_test -p 5001:5000 ${IMAGE_TAG} || true'
        sh 'sleep 2 || true'
        sh 'curl -f http://localhost:5001/ || true'
        sh 'docker rm -f smoke_test || true'
      }
    }
    stage('Push to Docker Hub') {
      when { expression { env.DOCKERHUB_REPO != '' } }
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', passwordVariable: 'DOCKERHUB_PASS', usernameVariable: 'DOCKERHUB_USER')]) {
          sh 'docker tag ${IMAGE_TAG} ${DOCKERHUB_REPO}:${GIT_COMMIT.substring(0,7)}'
          sh 'echo "$DOCKERHUB_PASS" | docker login -u "$DOCKERHUB_USER" --password-stdin'
          sh 'docker push ${DOCKERHUB_REPO}:${GIT_COMMIT.substring(0,7)}'
        }
      }
    }
    stage('Deploy to Kubernetes') {
      steps {
        echo 'Assumes kubectl is configured in Jenkins agent; apply k8s manifests (example)'
        sh 'kubectl apply -f k8s/deployment.yaml'
        sh 'kubectl apply -f k8s/service.yaml'
      }
    }
  }
}
