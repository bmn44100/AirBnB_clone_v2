#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir /data/
sudo mkdir /data/web_static/
sudo mkdir /data/web_static/releases/
sudo mkdir /data/web_static/shared/
sudo mkdir /data/web_static/releases/test/
echo "Hello World!" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
location_nginx="location /hbnb_static/ {\nalias /data/web_static/current/;\n}\n"
sudo sed -i "29i $location_nginx" /etc/nginx/sites-available/default
sudo service nginx restart
