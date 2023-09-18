#!/usr/bin/python3

from fabric.api import *

env.user = "ubuntu"
env.hosts = ['100.25.165.191']

def copy_file():
    """
    Copy ufw configuration file from the server to local machine
    """
    sudo("cat /etc/ufw/before.rules > /before.rules")
    get("/before.rules", "./")
