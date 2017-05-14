FROM python:3.5-alpine

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
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.4/main" >> /etc/apk/repositories && \
	  echo "http://dl-4.alpinelinux.org/alpine/v3.4/community" >> /etc/apk/repositories

RUN apk update && \
	apk add python py-pip curl unzip libexif udev chromium chromium-chromedriver xvfb && \
	pip install behave selenium pyvirtualdisplay PyHamcrest

COPY /features /opt/bdd
ADD behave.ini /opt/bdd

WORKDIR /opt/bdd
USER jenkins

ENTRYPOINT ["behave"]
