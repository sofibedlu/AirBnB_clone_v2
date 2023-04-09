#!/usr/bin/python3
"""creates and distributes an archive to your web servers,
    using the function deploy
"""
from datetime import datetime
from fabric.api import *

env.hosts = ['35.174.209.16', '35.153.226.72']


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder
    """
    command = """
    if [ ! -e versions ]
    then
        mkdir versions
    fi
    """
    local(command)
    now = datetime.now()
    created_time = now.strftime("%Y%m%d%H%M%S")
    name = "web_static_{}.tgz".format(created_time)
    result = local("tar -cvzf versions/{} web_static/".format(name))
    if result.failed:
        return None
    else:
        return 'versions/{}'.format(name)


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


def deploy():
    """fully deploy the statics to the web servers
    """

    path = do_pack()
    if not path:
        return False
    result = do_deploy(path)
    return result
