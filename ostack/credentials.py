'''

Specify credentials and access authenticated clients for
each OpenStack project.


'''
import novaclient.auth_plugin
import glanceclient.v1.client as glclient
import keystoneclient.v2_0.client as ksclient
from neutronclient.v2_0 import client as ntclient
import novaclient.v1_1.client as nvclient
import swiftclient.client as swclient
import os

_creds = {
    'auth_url': os.environ.get('OS_AUTH_URL', None),
    'username': os.environ.get('OS_USERNAME', None),
    'password': os.environ.get('OS_PASSWORD', None),
    'auth_system': os.environ.get('OS_AUTH_SYSTEM', None),
    'tenant_name': os.environ.get('OS_TENANT_NAME', None),
    'region_name': os.environ.get('OS_REGION_NAME', None),
    'swift_auth': os.environ.get('ST_AUTH', None),
    'swift_user': os.environ.get('ST_USER', None),
    'swift_key': os.environ.get('ST_KEY', None)
}


def set(auth_url, username, password, tenant_name, region_name=None,
        auth_system=None):
    """ Set OpenStack credentials

    By default, the credentials are read in from the environment. They
    can be overriden by this method.
    """
    _creds['auth_url'] = auth_url
    _creds['username'] = username
    _creds['password'] = password
    _creds['tenant_name'] = tenant_name
    _creds['region_name'] = region_name
    _creds['auth_system'] = auth_system


def set_swift(auth_url, user, key):
    """ Set Swift credentials

    Use this method to set Swift credentials when not using keystone
    """
    _creds['swift_auth'] = auth_url
    _creds['swift_user'] = user
    _creds['swift_key'] = key


def keystone():
    """ Retrive an authenticated keystone client """
    return ksclient.Client(auth_url=_creds['auth_url'],
                           username=_creds['username'],
                           password=_creds['password'],
                           tenant_name=_creds['tenant_name'],
                           region_name=_creds['region_name'],
                           auth_system=_creds['auth_system'])


def glance():
    """ Retrieve an authenticated glance client """
    ks = keystone()
    glance_endpoint = ks.service_catalog.url_for(service_type='image',
                                                 endpoint_type='publicURL')
    return glclient.Client(glance_endpoint, token=ks.auth_token)


def nova():
    """ Retrieve an authenticated nova client """
    auth_system = _creds['auth_system']
    if auth_system and auth_system != "keystone":
        auth_plugin = novaclient.auth_plugin.load_plugin(auth_system)
    else:
        auth_plugin = None

    return nvclient.Client(auth_url=_creds['auth_url'],
                           username=_creds['username'],
                           api_key=_creds['password'],
                           project_id=_creds['tenant_name'],
                           region_name=_creds['region_name'],
                           auth_system=_creds['auth_system'],
                           auth_plugin=auth_plugin)


def neutron():
    """ Retrieve an authenticated neutron client """
    return ntclient.Client(auth_url=_creds['auth_url'],
                           username=_creds['username'],
                           password=_creds['password'],
                           tenant_name=_creds['tenant_name'],
                           region_name=_creds['region_name'],
                           auth_system=_creds['auth_system'])


def swift():
    """ Retrieve an authenticated swift client """
    # If Swauth is defined, we use that, otherwise we use keystone auth
    if _creds['swift_auth']:
        return swclient.Connection(authurl=_creds['swift_auth'],
                                   user=_creds['swift_user'],
                                   key=_creds['swift_key'])
    else:
        return swclient.Connection(authurl=_creds['auth_url'],
                                   user=_creds['username'],
                                   key=_creds['password'])
