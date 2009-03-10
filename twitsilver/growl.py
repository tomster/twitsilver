from Growl import GrowlNotifier

def twitsilver_growl():
    """docstring for twitsilver_growl"""
    return GrowlNotifier('Twitsilver', ['failure', 'success'], 'success')