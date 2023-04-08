#!/usr/bin/python3
"""fabric script distributes the archive to web servers
    using the function do_deploy
    based on the file 1-pack_web_static.py
"""

from fabric.api import *


env.hosts = ['35.174.209.16', '35.153.226.72']


def do_deploy(archive_path):
    """deploy archive files to the remote host
    """
    archive_path = str(archive_path)
    try:
        put(archive_path, "/tmp/")
    except FileNotFoundError:
        return False
    folder = archive_path.split('/')[1].split('.')[0]
    file_name = archive_path.split('/')[1]
    sudo(" mkdir -p /data/web_static/releases/{}".format(folder))
    sudo("tar -xzvf /tmp/{} -C /data/web_static/releases/{}/\
            --strip-components=1".format(file_name, folder))
    sudo("rm /tmp/{}".format(file_name))
    sudo("rm /data/web_static/current")
    path = "/data/web_static/releases/{}/".format(folder)
    sudo("ln -s {} /data/web_static/current".format(path))
    return True
