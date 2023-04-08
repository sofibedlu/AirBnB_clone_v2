#!/usr/bin/python3
"""define do_pack method
"""

from datetime import datetime
from fabric.api import *


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
