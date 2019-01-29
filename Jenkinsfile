pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                withCredentials([usernamePassword(credentialsId: '063b1963-deff-4b3c-99e8-6fe71a2ce683', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh 'set +x'
                    // available as an env variable, but will be masked if you try to print it out any which way
                    // note: single quotes prevent Groovy interpolation; expansion is by Bourne Shell, which is what you want
                    sh 'echo $PASSWORD'
                    // also available as a Groovy variable
                    echo USERNAME
                    // or inside double quotes for string interpolation
                    echo "username is $USERNAME"
                    sh 'pwd'
                    sh 'python main.py $USERNAME $PASSWORD'
                }
                sh '$TENANCY_NUMBER'
                sh '$TENANCY_OWNER'
            }
        }
    }
}