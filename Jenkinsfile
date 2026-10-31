
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Construyendo la aplicacion Flask...'
            }
        }

        stage('Test') {
            steps {
                echo 'Ejecutando comprobaciones de la aplicacion...'
            }
        }

        stage('Analyze') {
            steps {
                script {
                    def scannerHome = tool 'SonarScanner'

                    withSonarQubeEnv('SonarQube') {
                        sh """
                            ${scannerHome}/bin/sonar-scanner \
                            -Dsonar.projectKey=proyecto-devsecops \
                            -Dsonar.projectName='Proyecto DevSecOps' \
                            -Dsonar.sources=. \
                            -Dsonar.sourceEncoding=UTF-8
                        """
                    }
                }
            }
        }

        stage('Security Test') {
            steps {
                echo 'Preparando los analisis de seguridad con OWASP...'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Preparando el despliegue de la aplicacion...'
            }
        }
    }
}
