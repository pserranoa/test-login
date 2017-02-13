FROM python:2.7-alpine

#===================
# environment
#===================
ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true
ENV DISPLAY :0.0

#===================
# Jenkins user
#===================
ARG user=jenkins
ARG group=jenkins
ARG uid=1000
ARG gid=1000
ENV BEHAVE_HOME /opt/bdd
RUN addgroup -g ${gid} ${group} && \
    adduser -u ${uid-} -D -G ${group} -s /bin/bash ${user} && \
    mkdir -p $BEHAVE_HOME && \
    chown $user:$group $BEHAVE_HOME

#===================
# Requisites
#===================
RUN \
  apk update && \
  apk add xvfb dbus-x11 firefox-esr ttf-freefont && \
  pip install behave>=1.2.5 selenium==2.52.0 pyvirtualdisplay>=0.1.5 PyHamcrest>=1.8

COPY /features /opt/bdd
ADD behave.ini /opt/bdd

WORKDIR /opt/bdd
USER jenkins

ENTRYPOINT ["behave"]
