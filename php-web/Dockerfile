FROM php:7.1-apache

WORKDIR /var/www/html
COPY . /var/www/html

RUN mkdir files
RUN chmod 755 /var/www/html/files
RUN chown www-data:www-data /var/www/html/files

RUN chmod 555 /var/www/html
RUN chown root:root /var/www/html

USER www-data