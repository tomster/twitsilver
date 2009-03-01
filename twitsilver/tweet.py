#!/usr/bin/env python
# encoding: utf-8
"""
tweet.py

Created by Tom Lazar on 2009-03-01.
Copyright (c) 2009 tomster.org. All rights reserved.
"""

import sys
from Growl import GrowlNotifier
from twitter import Twitter
growl = GrowlNotifier('Tweeter', ['failure', 'success'], 'success')
growl.register()

from keychain import Keychain

MAX_MSG = 140
FALLBACK_KEY = 'twitter'
AGENT_STR = "twittercommandlinetoolpy"

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
    if len(message) > MAX_MSG:
        growl.notify("failure", "Message too long", "%d characters, %d allowed." %
            (len(message), MAX_MSG))
        return

    # get credentials:
    keychain = Keychain()
    credentials = keychain.getgenericpassword('login', servicename='Twitterrific')
    # getgenericpassword returns a tuple upon error but a dict on success, duh:
    if type(credentials) == type(tuple):
        # if Twitterific hasn't stored credentials, we try a generic key
        credentials = keychain.getgenericpassword('login', item=FALLBACK_KEY)
    if type(credentials) == type(tuple):
        # notify the user about where to store credentials, if none are stored
        growl.notify("failure", "No credentials", 
        "Please add username/password to your login keychain with the item name '%s'" \
        % FALLBACK_KEY,
        sticky=True)
        return

    # post the message
    twit = Twitter(credentials['account'], credentials['password'], agent=AGENT_STR)
    message = (message.encode('utf8', 'replace'))
    twit.statuses.update(status=message)
    growl.notify("success", "Tweet sent.", message)

if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception, excp:
        growl.notify("failure", "Oops!", excp.message, sticky=True)