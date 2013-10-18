# ostack


Humane Python bindings for OpenStack

## Usage

    import ostack.credentials
    import ostack.containers
    import ostack.keypairs
    import ostack.images
    import ostack.instances
    import ostack.floating_ips

    ostack.credentials.set(...) # Optional, loads from env by default
    keypair = ostack.keypairs.create('mykey', os.path.expanduser('~/.ssh/id_rsa.pub'))
    for image in ostack.images.list():
       print image.name
    cirros = ostack.images.get(name='cirros')
    instance = ostack.instances.create(...)
    ip = ostack.floating_ips.create(...)
    instance.ports[0].set_floating_ip(ip)
    for container in ostack.containers.list():
      print container.name
    for obj in containers.get('mycontainer'):
      print obj.name
