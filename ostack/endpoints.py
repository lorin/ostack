from . import credentials


def get(service_type, endpoint_type='publicURL'):
    """ Retrieve the service endpoint URL """
    ks = credentials.keystone()
    return ks.service_catalog.url_for(service_type=service_type,
                                      endpoint_type=endpoint_type)


def image():
    """ Retrieve the image service (glance) endpoint """
    return get('image')


def identity():
    """ Retrieve the identity service (keystone) endpoint """
    return get('identity')


def compute():
    """ Retrieve the compute service (nova) endpoint """
    return get('compute')


def network():
    """ Retrieve the network service (neutron) endpoint """
    return get('network')


def volume():
    """ Retrieve the volume service (cinder) endpoint """
    return get('volume')
