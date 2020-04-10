#!/usr/bin/python3
"""
Fabric script
"""
from fabric.api import local
from datetime import datetime
import os


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
