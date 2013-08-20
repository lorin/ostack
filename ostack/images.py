import __builtin__

from .credentials import glance



def list():
    """ Return a list of glanceclient.v1.images.Image objects"""
    return __builtin__.list(glance().images.list())
