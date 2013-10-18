from .credentials import swift


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
        return [Object(**x) for x in swift().get_container(self.name)[1]]

class Object(object):
    """ A swift object """
    def __init__(self, name, bytes=None, last_modified=None, hash=None,
                 content_type=None):
        self.name = name
        self.bytes = bytes
        self.last_modified = last_modified
        self.hash = hash
        self.content_type = content_type

    def __repr__(self):
        return self.name


def list():
    """ Return a list of Swift containers """
    return [Container(**x) for x in swift().get_account(full_listing=True)[1]]


def get(name):
    """ Return a Swift container """
    return Container(name=name)
