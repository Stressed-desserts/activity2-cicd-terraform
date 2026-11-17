pipeline {
    agent any

    environment {
        AWS_DEFAULT_REGION = 'ap-south-1'
    }

    stages {
        stage('Checkout from GitHub') {
            steps {
                echo 'Retrieving source code from GitHub repository...'
                checkout scm
            }
        }

        stage('Build Application') {
            steps {
                dir('app') {
                    bat '''
                        python -m venv venv
                        call venv\\Scripts\\activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Automated Tests') {
            steps {
                dir('app') {
                    bat '''
                        call venv\\Scripts\\activate
                        pytest test_app.py -v --junitxml=test-reports/results.xml
                    '''
                }
            }
            post {
                always {
                    junit allowEmptyResults: true, testResults: 'app/test-reports/results.xml'
                }
            }
        }

        stage('Terraform Validate & Plan') {
            steps {
                dir('terraform') {
                    bat '''
                        terraform init -backend=false
                        terraform validate
                        terraform plan -input=false
                    '''
                }
            }
        }
    }

    post {
        success {
            echo "Activity 2 Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline execution failed. Review console logs."
        }
    }
}
