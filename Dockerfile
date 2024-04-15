FROM python:3.11.0-slim-bullseye

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y \
    apache2 \
    libmariadb-dev \
    libapache2-mod-wsgi-py3 \
    pkg-config \
    gcc 

# Configure timezone
ENV TZ=America/Mexico_City
RUN ln -snf  /etc/l/usr/share/zoneinfo/$TZocaltime && echo $TZ > /etc/timezone

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
# COPY ./seguimiento.conf /etc/apache2/sites-available/

# RUN adduser --disabled-password user

# RUN chown www-data:www-data /app/log
# RUN chown www-data:www-data /app/err_log

# RUN a2ensite seguimiento.conf


RUN pip3 install --upgrade pip
RUN pip3 install -r /app/requirements.txt

EXPOSE 80

CMD [ "apachectl", "-DFOREGROUND" ]


