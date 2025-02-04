pipeline {
    agent any // Specifies that this pipeline can run on any available agent
    environment{
        repository = 'sincerejisoo/wordpress-k8s'  // Docker Hub repository name
        DOCKERHUB_CREDENTIALS = 'dockerhub-jenkins' // Jenkins credentials ID for Docker Hub
        dockerImage = ''  // Placeholder for the Docker image name
    }

    stages { 
        stage('Building our image') { 
            steps { 
                script { 
                    sh "cp /var/lib/jenkins/workspace/sue_jenkins_project/build/libs/sue-member-0.0.1-SNAPSHOT.war /var/lib/jenkins/workspace/pipeline/" // war 파일을 현재 위치로 복사 
                    dockerImage = docker.build repository + ":latest" 
                }
            } 
        }
        stage('Login'){
            steps{
                sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin" // docker hub 로그인
            }
        }
        stage('Deploy our image') { 
            steps { 
                script {
                    // sh 'docker push $repository:$BUILD_NUMBER' // docker push
                    sh "docker push $repository:latest"
                } 
            }
        } 
        stage('Cleaning up') { 
            steps { 
                sh "docker rmi $repository:latest" // docker image 제거
            }
        } 
    }
}