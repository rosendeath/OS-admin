FROM jenkins/jenkins:lts

USER root

RUN apt-get update && apt-get install -y rpm dpkg git sudo curl && apt-get clean

USER jenkins