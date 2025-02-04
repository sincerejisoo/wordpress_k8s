pipeline {
    agent any // Specifies that this pipeline can run on any available agent
    environment{
        repository = 'sincerejisoo/wordpress-k8s'  // Docker Hub repository name
        DOCKERHUB_CREDENTIALS = 'dockerhub-jenkins' // Jenkins credentials ID for Docker Hub
        dockerImage = ''  // Placeholder for the Docker image name
    }


    stages { 
        stage('Checkout SCM'){
            steps{
                checkout scm
            }
        }
        stage('Login'){
            steps{
                script {
                    withCredentials([usernamePassword(credentialsId: "dockerhub-jenkins", 
                                                     usernameVariable: 'DOCKERHUB_CREDENTIALS_USR', 
                                                     passwordVariable: 'DOCKERHUB_CREDENTIALS_PSW')]) {
                        sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                    }
                }
            }
        }
        stage('Building our image') { 
            steps { 
                script { 
                    sh "docker build -t $repository:latest ." // docker build
                }
            } 
        }
        stage('Deploy our image') { 
            steps { 
                script {
                    // sh "docker tag $repository:latest $repository:$BUILD_NUMBER" // docker image tag
                    sh "docker push $repository:latest"
                } 
            }
        } 
        stage('Cleaning up') { 
            steps { 
                sh "docker rmi $repository:latest" // docker image 제거
            }
        } 
        stage('Deploy to Kubernetes') { 
            steps { 
                script { 
                    sh "kubectl rollout restart deploy/wordpress" // k8s deployment
                }
            }
        }
    }
}