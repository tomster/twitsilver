#!/usr/bin/env python
# encoding: utf-8
"""
tweet.py

Created by Tom Lazar on 2009-03-01.
Copyright (c) 2009 tomster.org. All rights reserved.
"""

import sys
from Growl import GrowlNotifier
growl = GrowlNotifier('Tweeter', ['failure', 'success'], 'success')

MAX_MSG = 140
#growl.register()

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        message = argv[1]
    except IndexError:
        message = None

    if not message:
        growl.notify("failure", "No message", "You need to actually say something!")
        return
    
    # Check length
    # TODO: use URL shortening service
    if len(message) > 140:
        growl.notify("failure", "Message too long", "%d characters, %d allowed." %
            (len(message), MAX_MSG))
        return

    growl.notify("success", "You said", message)

if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception, excp:
        growl.notify("failure", "Uncaught exception", str(excp))