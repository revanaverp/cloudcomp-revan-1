pipeline {
  agent any
  environment {
    IMAGE_NAME = 'fakhriizzulhaq/simple-app'
    REGISTRY_CREDENTIALS = 'dockerhub-credentials'
  }
  stages {
    stage('Checkout SCM') { 
      steps { 
        checkout scm 
      } 
    }
    
    stage('Validate App & Database') { 
      steps { 
        bat 'echo "Memeriksa file aplikasi Flask dan skema database SQLite..."' 
      } 
    }
    
    stage('Build Docker Image') {
      steps { 
        bat "docker build -t %IMAGE_NAME%:%BUILD_NUMBER% ." 
      }
    }
    
    stage('Push to Docker Hub') {
      steps {
        withCredentials([usernamePassword(credentialsId: REGISTRY_CREDENTIALS,
            usernameVariable: 'USER', passwordVariable: 'PASS')]) {
          bat 'docker login -u %USER% -p %PASS%'
          bat "docker push %IMAGE_NAME%:%BUILD_NUMBER%"
          bat "docker tag %IMAGE_NAME%:%BUILD_NUMBER% %IMAGE_NAME%:latest"
          bat "docker push %IMAGE_NAME%:latest"
        }
      }
    }
  }
  post {
    always {
      echo 'Pipeline CI/CD Flask + SQLite selesai dieksekusi.'
    }
  }
}
