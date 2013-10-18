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
        return [Object(container=self.name, **x) for x in
                swift().get_container(self.name)[1]]


class Object(object):
    """ A swift object.

    Can be initialized by specifying a path (including container),
    or workflow/container separately
    """
    def __init__(self, path=None, container_name=None, name=None, bytes=None,
                 last_modified=None, hash=None, content_type=None):
        if path is not None:
            (self.container_name, self.name) = path.split('/', 1)
        else:
            self.container_name = container_name
            self.name = name
        self.bytes = bytes
        self.last_modified = last_modified
        self.hash = hash
        self.content_type = content_type

    def __repr__(self):
        return self.name

    @property
    def path(self):
        return "{}/{}".format(self.container_name, self.name)

    @property
    def url(self):
        """ Return the full url for this object """
        storage_url, _ = swift().get_auth()
        s = "{storage_url}/{path}"
        return s.format(storage_url=storage_url,
                        path=self.path)

    def temp_url(self):
        """ Generate a temporary url """
        pass


def list():
    """ Return a list of Swift containers """
    return [Container(**x) for x in swift().get_account(full_listing=True)[1]]


def get(name):
    """ Return a Swift container """
    return Container(name=name)
