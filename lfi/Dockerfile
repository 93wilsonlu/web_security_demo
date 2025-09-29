FROM php:7.1-apache

WORKDIR /var/www/html

COPY . /var/www/html

# 建立 log 目錄並確保權限
RUN mkdir -p /var/log/apache2 && rm -f /var/log/apache2/* && \
    touch /var/log/apache2/access.log /var/log/apache2/error.log && \
    chown -R www-data:www-data /var/log/apache2 /var/www/html

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
