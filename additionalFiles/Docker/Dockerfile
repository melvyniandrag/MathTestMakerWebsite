FROM ubuntu

RUN mkdir -p /home/teacher/MathTestMakerWebsite
RUN mkdir -p /home/MathTestMaker
WORKDIR /home/teacher/MathTestMakerWebsite
ADD 000-default.conf /home/teacher/MathTestMakerWebsite
ADD permissionScript.sh /root

# apt installs
RUN apt-get -y update
RUN apt-get -y install vim
RUN apt-get -y install apache2 curl libapache2-mod-wsgi-py3
RUN apt-get -y install python3-dev python3-pip

# pip3 installs
RUN pip3 install psycopg2-binary
RUN pip3 install python-dateutil
RUN pip3 install Django==2.1.1
RUN pip3 install stripe
RUN pip3 install djangorestframework

# server config

# Apache config
RUN mv 000-default.conf /etc/apache2/sites-available/000-default.conf
RUN chmod 777 /root/permissionScript.sh

# startup command
CMD /root/permissionScript.sh && a2enmod ssl && service apache2 start && /bin/bash
