#!/usr/bin/python3
"""
Fabric script 
"""
from fabric.api import env
from fabric.api import local
from datetime import datetime
import os


env.hosts = ['35.196.219.244', '54.226.69.66']

def do_pack():
    """web_static"""
    t = datetime.now().strftime("%Y%m%d%H%M%S")
    f = "versions/web_static_" + t + ".tgz"
    local("mkdir -p versions")
    local("tar -cvzf " + f + " web_static")
    if not (os.path.exists(f)):
        return None
    else:
        return f


def do_deploy(archive_path):
    """web servers"""
    if not os.path.exists(archive_path) and not os.path.isfile(archive_path):
        return False
    put(archive_path, '/tmp/')
    m = archive_path.replace('.tgz', '')
    m = m.replace('versions/', '')
    run('mkdir -p /data/web_static/releases/{}/'.format(m))
    run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/'
        .format(m, m))
    run('rm /tmp/{}.tgz'.format(m))
    run('mv /data/web_static/releases/{}/web_static/* '.format(m) +
        '/data/web_static/releases/{}/'.format(m))
    run('rm -rf /data/web_static/releases/{}/web_static'.format(m))
    run('rm -rf /data/web_static/current')
    run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
        .format(m))
    print('New version successfuly deployed')
    return True
