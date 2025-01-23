FROM wordpress:php8.3-apache

COPY ./wp-config.php /var/www/html/wp-config.php

COPY ./wp-content/plugins /var/www/html/wp-content/plugins

COPY ./wp-cli.phar /usr/local/bin/wp

RUN chmod +x /usr/local/bin/wp

EXPOSE 80 443



# version: '3.1'

# services:
#   wordpress:
#     image: wordpress:php8.3-apache

#     ports:
#       - "8000:80"
#       - "44300:443"
#     volumes:
#       - ./wp-config.php:/var/www/html/wp-config.php
#       - ./wp-content/plugins:/var/www/html/wp-content/plugins
#       - ./wp-cli.phar:/usr/local/bin/wp
#     # environment:
#     #   WORDPRESS_DB_HOST: db
#     #   WORDPRESS_DB_USER: wp_admin
#     #   WORDPRESS_DB_PASSWORD: cicd1234
#     #   WORDPRESS_DB_NAME: wordpress_db
#     depends_on:
#       - db
#       - db_redis