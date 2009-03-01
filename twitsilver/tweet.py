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
#growl.register()

from keychain import Keychain

MAX_MSG = 140
FALLBACK_KEY = 'twitter'

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

    # get credentials:
    keychain = Keychain()
    username, password = keychain.getgenericpassword('login', servicename='Twitterrific')
    if not username:
        username, password = keychain.getgenericpassword('login', item=FALLBACK_KEY)
    if not username:
        growl.notify("failure", "No credentials", 
        "Please add username/password to your login keychain with the item name '%s'" % FALLBACK_KEY,
        sticky=True)
        return

    growl.notify("success", "You said", message)

if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception, excp:
        growl.notify("failure", "Uncaught exception", str(excp))