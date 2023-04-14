#!/usr/bin/python3
"""Fabric script that deletes out-of-date archives using
    a function do_clean
"""
from fabric.api import *

execute_local_command = True
env.hosts = ['35.174.209.16', '35.153.226.72']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_clean(number=0):
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
            local(command_local)
        execute_local_command = False
    with cd("/data/web_static/releases"):
        sudo(command_remote)
