#!/bin/bash
# Download installer
curl -sS https://getcomposer.org/installer | php
# Move to global path
sudo mv composer.phar /usr/local/bin/composer
composer install

sudo chown $(whoami):$(whoami) ./data.txt
sudo chmod 600 ./data.txt

cd raw-files
php -S localhost:8000 &
cd ..
python app.py