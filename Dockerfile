FROM wordpress:php8.3-apache

WORKDIR /var/www/html

COPY ./wp-config.php /var/www/html/wp-config.php

COPY ./wp-content/plugins /var/www/html/wp-content/plugins

COPY ./wp-cli.phar /usr/local/bin/wp
RUN chmod +x /usr/local/bin/wp

EXPOSE 80
EXPOSE 443