#!/usr/bin/python3
# Fabfile to create and distribute an archive to a web server.
from fabric.api import env
from fabric.api import local
from fabric.api import put
from fabric.api import run
from datetime import datetime
import os.path

env.hosts = ["100.25.117.101", "54.160.106.191"]


def do_pack():
    """ Creates a .tgz archive of the directory web_static
        Otherwise returns None
    """
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month, dt.day,
                                                         dt.hour, dt.minute,
                                                         dt.second)

    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file


def do_deploy(archive_path):
    """ Distributes an archive to my web server
        Otherwise returns False
    """
    if os.path.isfile(archive_path) is False:
        return False

    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("sudo rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("sudo mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name)).failed is True:
        return False
    if run("sudo rm /tmp/{}".format(file)).failed is True:
        return False

    if run("sudo mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("sudo rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("sudo rm -rf /data/web_static/current").failed is True:
        return False
    if run("sudo ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True


def deploy():
    """ Executes the creation and distribution of the archive to a server
    """
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
