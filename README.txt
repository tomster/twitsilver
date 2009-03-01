Twitsilver is a `Quicksilver <http://code.google.com/p/blacktree-alchemy/>`_ action for posting to `twitter <http://twitter.com/home>`_.

It features 

* `Growl <http://growl.info/>`_ support 
* `Keychain <http://en.wikipedia.org/wiki/Keychain_(Mac_OS)>`_ support
* easy two-step-installation.

Installation
============

Twitsilver installation is a two step process:

1. ``easy_install`` the code
2. custom install the Quicksilver action

This is because distutils (as a pure python, platform independant tool) doesn't know anything about Quicksilver actions. Therefore we create a quicksilver-aware installer on the Desktop for you.

In other words, open the Terminal (``/Applications/Utitlities/Terminal.app``) and execute the following two commands::

    sudo easy_install twitsilver
    install_twitsilver_action.py

If this fails due to missing ``PATH`` entries, you need to find the ``install_twitsilver_action.py`` script and execute it. Due to the sandbox restrictions of distutils it can't be copied to a more convenient location.

After that you need to restart Quicksilver (Command-Control-q) and you're good to go.

Usage
=====

Now you can invoke Quicksilver and press ``.`` to enter text mode. Type the message you want to post to twitter, hit the tab key and start to type ``tweet`` until the action shows up. Now just hit enter to invoke the it.

Credentials
***********

Twitsilver uses the Mac OS X Keychain to know which username and password to use. It first checks, whether `Twitterrific <http://iconfactory.com/software/twitterrific>`_ has any credentials stored and if so, it uses those.

If not, it falls back to an item by the name of ``twitter``. To create this entry, open up *Keychain Access* and add a new password item (Command-n), give it the name ``twitter`` and your username and password.

Growl
*****

Theoretically, twitsilver should also work *without* Growl, but this hasn't been tested, as there is no sane reason any Mac OS X user should *not* install this insanely useful utility :-)

After contacting twitter and posting the message twitsilver will use Growl to notify you that it has succeeded. If not, it will post twitters error message.

Of course, twitsilver checks the length of your message and will refuse to post it, if it's longer than the infamous 140 characters.

TODO
====

* Currently twitsilver registers itself with Growl for *every* call. Ideally, this should be done only once, upon installation
* use an URL shortening service to shorten any URLs *before* posting to twitter.
* add a nicer icon (for growl)
* twitsilver has no pony. This is unacceptable in the long run

