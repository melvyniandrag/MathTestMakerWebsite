FROM debian:bookworm

RUN apt -y update

RUN apt -y upgrade

RUN apt -y install python3-dev python3-pip apache2 libapache2-mod-wsgi-py3

RUN apt -y install python3-django python3-stripe
 
COPY mathtestmaker.com.conf /etc/apache2/sites-available

COPY MathTestMaker /var/www/MathTestMaker

COPY MathTestMakerLibrary /MathTestMakerLibrary

WORKDIR /var/www/MathTestMaker

RUN a2enmod wsgi

RUN a2dissite 000-default.conf

RUN a2ensite mathtestmaker.com.conf

EXPOSE 80
#CMD ["apachectl", "-D", "FOREGROUND"]
