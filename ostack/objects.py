import hmac
import time
import urlparse

from hashlib import sha1
from time import time

from .account import get_temp_url_key, set_temp_url_key
from .credentials import swift


class Object(object):
    """ A swift object.

    Can be initialized by specifying a full name (includes container),
    or container and name separately
    """
    def __init__(self, full_name=None, container_name=None, name=None,
                 bytes=None, last_modified=None, hash=None,
                 content_type=None):
        if full_name is not None:
            (self.container_name, self.name) = full_name.split('/', 1)
        else:
            self.container_name = container_name
            self.name = name
        self.bytes = bytes
        self.last_modified = last_modified
        self.hash = hash
        self.content_type = content_type
        self._url = None  # cached url

    def __repr__(self):
        return self.name

    @property
    def full_name(self):
        """ Object name with container name prepended.

        Note that this does not contain version name or account name

        >>> Object(container_name='foo', name='baz/quux.png').path
        'foo/baz/quux.png'
        """
        return "{}/{}".format(self.container_name, self.name)

    @property
    def path(self):
        """ Return the full path of the url.

        >>> obj = Object(...)
        >>> obj.path
        '/v1/AUTH_a922ead7-1df8-42c1-8a39-226aff4223a4/'
        """
        return urlparse.urlparse(self.url).path

    @property
    def url(self):
        """ Return the full url for this object """
        # We cache the url so we don't need to do a lookup every time
        if self._url is None:
            storage_url, _ = swift().get_auth()
            s = "{storage_url}/{full_name}"
            self._url = s.format(storage_url=storage_url,
                            full_name=self.full_name)
        return self._url

    def generate_temp_url(self, expires=int(time()+60*60*24),
                          method='GET'):
        """ Generate a temporary url for this object

        expires is in Unix time.

        Default expiry is 24 hours after this method is called

        By default, allows GET only"""

        # If the secret key exists, retrieve it. Otherwise, generate it
        try:
            key = get_temp_url_key()
        except KeyError:
            key = set_temp_url_key()

        hmac_body = '%s\n%s\n%s' % (method, expires, self.path)
        sig = hmac.new(key, hmac_body, sha1).hexdigest()
        s = '{url}?temp_url_sig={sig}&temp_url_expires={expires}'
        return s.format(url=self.url, sig=sig, expires=expires)
