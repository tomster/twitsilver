#!/usr/bin/env python
from os import path, mkdir, chmod
import sys

from growl import twitsilver_growl

def install_action():
    """ Installs the Quicksilver action """
    DEST_DIR = path.join(path.expanduser("~"), 
        "Library/Application Support/Quicksilver/Actions")

    if not path.exists(DEST_DIR):
        print "Creating target directory!" ; 
        mkdir(DEST_DIR)

    print "Installing Quicksilver action"
    installer = """#!/usr/bin/env python
# encoding: utf-8
__requires__ = 'twitsilver'
import sys
from pkg_resources import load_entry_point

sys.exit(
   load_entry_point('twitsilver', 'console_scripts', 'tweet')()
)
    """
    installer_script = open(DEST_DIR + "/tweet.py", 'w')
    installer_script.write(installer)
    installer_script.close()
    chmod(DEST_DIR + "/tweet.py", 0775)

def register_growl():
    """Register with the growl service"""
    print "Registering with growl."
    twitsilver_growl().register()

def main(argv=None):
    install_action()
    register_growl()
    print "Done! Now restart Quicksilver (command-control-q)"
    
    

if __name__ == "__main__":
    sys.exit(main())
