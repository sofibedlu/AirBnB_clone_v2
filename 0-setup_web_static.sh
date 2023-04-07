#!/usr/bin/env bash
#a script that sets up the web servers for the deployment of web_static

if ! dpkg-query -W -f='${Status}' nginx 2>/dev/null | grep -q "install ok installed";
then
        sudo apt-get update
        sudo apt-get -y install nginx
fi
if [ ! -d "/data/" ]
then
        sudo mkdir -p /data/
fi
if [ ! -d "/data/web_static/" ]
then
        sudo mkdir -p /data/web_static/
fi
if [ ! -d "/data/web_static/releases/" ]
then
        sudo mkdir -p /data/web_static/releases/
fi
if [ ! -d "/data/web_static/shared/" ]
then
        sudo mkdir -p /data/web_static/shared/
fi
if [ ! -d "/data/web_static/releases/test/" ]
then
        sudo mkdir -p /data/web_static/releases/test/
fi

sudo echo "test nginx config/hello_world" | sudo tee /data/web_static/releases/test/index.html

link="/data/web_static/current"
target="/data/web_static/releases/test/"
if [ -e "$link" ]
then
        sudo rm /data/web_static/current
        sudo ln -s $target $link
else
        sudo ln -s $target $link
fi

sudo chown -R ubuntu:ubuntu /data/

server_b="\
server {\n\
\tlisten 80;\n\
\tserver_name holb2023eah4hz.tech localhost;\n\
\n\
\tlocation /hbnb_static/ {\n\
\t\talias /data/web_static/current/;\n\
\t}\n\
}"

sudo echo -e "$server_b" | sudo tee /etc/nginx/sites-available/holb2023eah4hz.tech

if [ -e "/etc/nginx/sites-enabled/holb2023eah4hz.tech" ]
then
        sudo rm /etc/nginx/sites-enabled/holb2023eah4hz.tech
fi
sudo ln -s /etc/nginx/sites-available/holb2023eah4hz.tech /etc/nginx/sites-enabled/

sudo service nginx restart
