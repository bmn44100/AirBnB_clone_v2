#!/usr/bin/python3
"""
module for a Fabric script that generates a .tgz archive
from the contents of the web_static folder of
your AirBnB Clone repo, using the function do_pack
"""
from fabric.api import *
from datetime import datetime
import os


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
        print("web_static packed: versions/{} -> {}".
              format(static_archive, os.path.getsize(static_archive)))
    except BaseException:
        return None
