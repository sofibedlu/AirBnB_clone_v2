#!/usr/bin/python3
"""creates and distributes an archive to your web servers,
    using the function deploy
"""
do_deploy = __import__('2-do_deploy_web_static').do_deploy
do_pack = __import__('1-pack_web_static').do_pack


def deploy():
    """fully deploy the statics to the web servers
    """

    path = do_pack()
    if not path:
        return False
    result = do_deploy(path)
    return result
