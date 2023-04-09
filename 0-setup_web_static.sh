#!/usr/bin/env bash
#a script that sets up the web servers for the deployment of web_static

if ! dpkg-query -W -f='${Status}' nginx 2>/dev/null | grep -q "install ok installed";
then
        sudo apt-get update
        sudo apt-get -y install nginx
fi

#create dir
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

#dumy html for testing
sudo echo "test nginx config/hello_world" | sudo tee /data/web_static/releases/test/index.html

#create symbolic link
link="/data/web_static/current"
target="/data/web_static/releases/test"
if [ -e "$link" ]
then
        sudo rm /data/web_static/current
        sudo ln -sf $target $link
else
        sudo ln -sf $target $link
fi

#change ownership
sudo chown -R ubuntu:ubuntu /data/

SERVER_CONFIG=\
"server {
	listen 80 default_server;
	listen [::]:80 default_server;
	root /var/www/html;
        error_page 404 /404.html;
	index index.html index.htm index.nginx-debian.html;
	server_name _;
	if (\$request_filename ~ redirect_me){
		rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
	}
	location / {
		try_files \$uri \$uri/ =404;
	}
	location /hbnb_static/ {
		alias /data/web_static/current/;
	}
}"

#update server block
sudo bash -c "echo -e '$SERVER_CONFIG' | sudo tee /etc/nginx/sites-enabled/default"

#enable server blocks
sudo ln -sf '/etc/nginx/sites-available/default' '/etc/nginx/sites-enabled/default'
sudo service nginx restart
