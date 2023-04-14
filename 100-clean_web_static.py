#!/usr/bin/python3
"""Fabric script that configure and distribute archives to
    remote hosts
"""
from datetime import datetime
from fabric.api import *

"""execute_local_command = True"""
env.hosts = ['35.174.209.16', '35.153.226.72']
"""
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'
"""


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
    sudo("mkdir -p /data/web_static/releases/{}".format(folder))
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


"""
def do_clean(number=0):
    ""/"Deletes out-of-date archives of the static files.
    Args:
        number (Any): The number of archives to keep.
    "/""
    global execute_local_command
    number = int(number)
    if number < 0:
        return
    if number == 0:
        number = 1
    lines = "ls -l versions | tail -n +2 | wc -l"
    num_lines_l = local(lines, capture=True)
    num_lines_l = int(num_lines_l.stdout.strip())
    net_line = num_lines_l - number

    lines_remote = "ls -l /data/web_static/releases | tail -n +2 | wc -l"
    num_lines_r = run(lines_remote)
    num_lines_r = int(num_lines_r.stdout.strip())
    net_line_r = num_lines_r - number
    command_local = f"ls -lt | tail -n +2 | tail -n {net_line} | cut -d ' '\
            -f 9 | xargs rm"
    command_remote = f"ls -lt | tail -n +2 | tail -n {net_line_r} | cut -d ' '\
            -f 9 | xargs rm -rf"

    if execute_local_command:
        with lcd("./versions"):
            ""/"execute command versions"/""
            local(command_local)
        execute_local_command = False
    with cd("/data/web_static/releases"):
        ""/"execute command in remote"/""
        sudo(command_remote)
        """
