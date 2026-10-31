
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
                            -Dsonar.projectKey=Proyecto-DevSecOps \
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
               dependencyCheck additionalArguments: '--scan . --enableExperimental --format ALL --out dependency-check-report', odcInstallation: 'Dependency-Check-12.2.2'

                dependencyCheckPublisher pattern: 'dependency-check-report/dependency-check-report.xml'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Preparando el despliegue de la aplicacion...'
            }
        }
    }
}
