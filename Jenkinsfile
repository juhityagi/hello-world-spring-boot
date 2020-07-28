def project="${JOB_NAME}".split('/')[0]
pipeline {
  agent none
  environment {
    PROJECT_NAME= "${project}"
  }
  stages {
    stage("build & SonarQube analysis") {
      agent any
      steps {
        withSonarQubeEnv('sonar') {
          sh 'mvn clean package sonar:sonar'
        }
      }
    }
    stage ("SonarQube analysis") { 
      agent none
      steps { 
       
        catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
          script {
            def qualitygate = waitForQualityGate() 
            if (qualitygate.status != "OK") { 
              error "Pipeline aborted due to quality gate coverage failure: ${qualitygate.status}" 
            }
          }
        }
        
      } 
    }
    stage('Saving Logs') {
      agent any
      steps {
          sh 'printenv'
          sh 'echo "Saving logs to a new file in ${JENKINS_HOME}/LOGS folder..."'
          sh 'cat ${JENKINS_HOME}/jobs/${JOB_NAME}/builds/${BUILD_NUMBER}/log >> ${BUILD_TAG}.txt'
          sh 'pwd'
          sh 'python3 /usr/local/hello-world-spring-boot/generate.py ${BUILD_TAG}.txt'
          sh 'mkdir ${WORKSPACE}/target/surefire-reports/unit-test'
          sh 'cp ${WORKSPACE}/target/surefire-reports/*.txt ${WORKSPACE}/target/surefire-reports/unit-test'
          sh 'ls ${WORKSPACE}/target/surefire-reports/unit-test'
      }
    }
  }
}

