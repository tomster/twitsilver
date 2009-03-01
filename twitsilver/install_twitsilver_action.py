#!/usr/bin/env python
from os import path, mkdir, chmod
import sys

def main(argv=None):
    DEST_DIR = path.join(path.expanduser("~"), "Library/Application Support/Quicksilver/Actions")

    if not path.exists(DEST_DIR):
        print "creating target directory!" ; 
        mkdir(DEST_DIR)

    print "installing Quicksilver action"
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
    print "Done! Now restart Quicksilver (command-control-q)"

if __name__ == "__main__":
    sys.exit(main())
