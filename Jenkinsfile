pipeline {
    agent any
    triggers {
        cron('H 13 * * *')
    }
    stages {
        stage('Testing') {
            steps {
                echo 'Start Testing'
                bat '''
                    if not exist venv virtualenv venv
                    call venv\\Scripts\\activate.bat
                    pip install -r requirements.txt
                    pytest -n 1 --env=dev --headless=True -m smoke --html=report/report-${BUILD_NUMBER}.html
                    exit %ERRORLEVEL%
                    deactivate
                '''
            }
        }
    }
    post{
        failure {
            emailext body: '''${SCRIPT, template="groovy-html.template"}''',
                mimeType: 'text/html',
                subject: "[Jenkins] ${currentBuild.fullDisplayName}",
                to: "yan.liu@mullenloweprofero.com",
                replyTo: "yan.liu@mullenloweprofero.com",
                recipientProviders: [[$class: 'CulpritsRecipientProvider']]
        }
		always {
			echo 'Complete!'
		}
	}
}