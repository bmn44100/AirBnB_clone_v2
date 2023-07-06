#!/usr/bin/python3
"""
module for a Fabric script
that creates and distributes an archive to your web servers,
using the functions do_pack and do_deploy
"""
from fabric.api import *
from datetime import datetime
import os

env.hosts = ['34.207.253.67', '52.3.249.58']
env.user = 'ubuntu'


def do_pack():
    """
    function that creates an archive of hbnb clone static files
    """
    try:
        date = datetime.now()
        static_archive = "web_static_{}{}{}{}{}{}.tgz".\
                         format(date.year, date.month, date.day,
                                date.hour, date.minute, date.second)
        local("mkdir -p versions")
        local("tar -cvzf versions/{} web_static".format(static_archive))
        if os.path.exists("versions/{}".format(static_archive)):
            return "versions/{}".format(static_archive)
    except BaseException as e:
        print(e)
        return None

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
    except:
        return False

def deploy():
    """
    function deploy that Call the do_pack() function and
    do_deploy() function and creates and distributes an archive to your web servers
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    result = do_deploy(archive_path)
    return result
