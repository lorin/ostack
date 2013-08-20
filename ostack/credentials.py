import keystoneclient.v2_0.client as ksclient
import glanceclient.v1.client as glclient
import novaclient.v1_1.client as nvclient

import os

_creds = {
    'auth_url': os.environ.get('OS_AUTH_URL', None),
    'username': os.environ.get('OS_USERNAME', None),
    'password': os.environ.get('OS_PASSWORD', None),
    'tenant_name': os.environ.get('OS_TENANT_NAME', None),
    'region': os.environ.get('OS_REGION', None)
}


def set(auth_url, username, password, tenant_name, region=None):
    """ Set OpenStack credentials

    By default, the credentials are read in from the environment but they
    can be overriden by this method.
    """
    _creds['auth_url'] = auth_url
    _creds['username'] = username
    _creds['password'] = password
    _creds['tenant_name'] = tenant_name
    _creds['region'] = region


def keystone():
    """ Retrive an authenticated keystone client """
    return ksclient.Client(auth_url=_creds['auth_url'],
                           username=_creds['username'],
                           password=_creds['password'],
                           tenant_name=_creds['tenant_name'])


def glance():
    """ Retrieve an authenticated glance client """
    ks = keystone()
    glance_endpoint = ks.service_catalog.url_for(service_type='image',
                                                 endpoint_type='publicURL')
    return glclient.Client(glance_endpoint, token=ks.auth_token)


def nova():
    """ Retrieve an authenticated nova client """
    return nvclient.Client(auth_url=_creds['auth_url'],
                           username=_creds['username'],
                           api_key=_creds['password'],
                           project_id=_creds['tenant_name'])
