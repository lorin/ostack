# ostack


Humane Python bindings for OpenStack

## Usage

    >>> import ostack
    >>> ostack.credentials.set(...) # Optional, loads from env by default
    >>> keypair = ostack.keypairs.create('mykey', os.path.expanduser('~/.ssh/id_rsa.pub'))
    >>> for image in ostack.images.list():
    ...    print image.name
    >>> cirros = ostack.images.get(name='cirros')
    >>> instance = ostack.instances.create(...)
    >>> ip = ostack.floating_ips.create(...)
    >>> instance.ports[0].set_floating_ip(ip)
