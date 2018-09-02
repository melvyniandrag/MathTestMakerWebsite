FROM ubuntu

WORKDIR /root/MathTestMakerWebsite
ADD . /root/MathTestMakerWebsite

# apt installs
RUN apt-get -y update
RUN apt-get -y install vim
RUN apt-get -y install apache2 curl libapache2-mod-wsgi-py3
RUN apt-get -y install python3-dev python3-pip

# pip3 installs
RUN pip3 install psycopg2-binary
RUN pip3 install python-dateutil
RUN pip3 install pinax-stripe
RUN pip3 install Django==2.1.1

# server config

## Apache config
#RUN mv apache.conf /etc/apache2/sites-available/000-default.conf
#RUN chmod 755 /root/MathTestMakerWebsite
#RUN chown -R :www-data /root/MathTestMakerWebsite
#RUN chgrp -R :www-data /root/MathTestMakerWebsite
#
## startup command
#CMD a2enmod ssl && service apache2 start && /bin/bash

CMD /bin/bash
