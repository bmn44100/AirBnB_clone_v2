#!/usr/bin/python3
"""
module for a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers,
using the function do_deploy
"""
from fabric.api import *
from datetime import datetime
import os

env.hosts = ['34.207.253.67', '52.3.249.58']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """
    deploy web_static archive on your servers: xx-web-01 and xx-web-02
    """
    if os.path.exists(archive_path) is False:
        return False

    web_static_archive = archive_path.split("/")[1]
    web_static_file = archive_path.split(".")[0]
    uncompress_static = "/data/web_static/releases/{}/".format(web_static_file)

    try:
        put(archive_path, "/tmp")
        run("mkdir -p {}".format(uncompress_static))
        run("tar -xzf /tmp/{} -C {}".format(web_static_archive, uncompress_static))
        run("rm /tmp/{}".format(web_static_archive))
        run("mv {}/web_static/* {}".format(uncompress_static, uncompress_static))
        run("rm -rf {}/web_static".format(uncompress_static))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(uncompress_static))
        return True
    except BaseException:
        return False
