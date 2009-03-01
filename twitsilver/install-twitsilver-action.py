#!/usr/bin/env python
from os import path, mkdir, chmod

DEST_DIR = path.join(path.expanduser("~"), "Library/Application Support/Quicksilver/Actions")

if not path.exists(DEST_DIR):
    print "creating target directory!" ; 
    mkdir(DEST_DIR)

print "installing Quicksilver action"
installer = """
#!/usr/bin/env python
# encoding: utf-8
__requires__ = 'twitsilver>=0.1dev'
import sys
from pkg_resources import load_entry_point

sys.exit(
   load_entry_point('twitsilver==0.1dev', 'console_scripts', 'tweet')()
)
"""
installer_script = open(DEST_DIR + "/tweet.py", 'w')
installer_script.write(installer)
installer_script.close()
chmod(DEST_DIR + "/tweet.py", 755)
print "Done! Now restart Quicksilver (command-control-q)"
