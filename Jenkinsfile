pipeline {
    agent {
        docker {
            image 'my-jenkins'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    stages {
        stage('Clone repository') {
            steps {
                git branch: 'main', url: 'https://github.com/VasalIllia/System-programming-and-OS-administration.git'
            }
        }
        stage('Download DEB package') {
            steps {
                sh '''
                    curl -L https://github.com/VasalIllia/System-programming-and-OS-administration/raw/main/packages/count-files_1.0-2_amd64.deb -o /tmp/count-files_1.0-2_amd64.deb
                '''
            }
        }
        stage('Install DEB') {
            steps {
                sh '''
                    sudo dpkg -i /tmp/count-files_1.0-2_amd64.deb
                '''
            }
        }
        stage('Run script') {
            steps {
                sh '''
                    /usr/local/bin/count_files.sh
                '''
            }
        }
    }
}
