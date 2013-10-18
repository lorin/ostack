'''

Object Storage (Swift) containers

'''

from .credentials import swift
from .objects import Object


class Container(object):
    """ A Swift container """

    def __init__(self, name, count=None, bytes=None):
        self.name = name
        self.count = count
        self.bytes = bytes

    def __repr__(self):
        return "Container(name='{name}')".format(name=self.name)

    def list(self):
        """ List the objects in a container """
        return [Object(container=self.name, **x) for x in
                swift().get_container(self.name)[1]]


def list():
    """ Return a list of Swift containers """
    return [Container(**x) for x in swift().get_account(full_listing=True)[1]]
