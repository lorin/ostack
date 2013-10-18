.. ostack documentation master file, created by
   sphinx-quickstart on Wed Aug 21 19:55:45 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

******
ostack
******

ostack: Humane Python bindings for OpenStack
============================================


`ostack` is a Python API for OpenStack that sits on top of the native
bindings and provides a programming interface that makes it simpler to
do common OpenStack tasks.

::

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
    for obj in containers.Container('mycontainer'):
      print obj.name


Object storage (swift)
======================


List containers::

    from ostack import containers
    for container in containers.list():
      print container.name

List the contents of a container::

    from ostack import containers
    for obj in containers.Container('mycontainer'):
        print obj.name


Retrieve the url associated with an object::

    from ostack import objects
    obj = Object('mycontainer/path/to/object')
    print obj.url


Generate a temporary url to an object::

    from ostack import objects
    obj = Object('mycontainer/path/to/object')
    print obj.generate_temp_url()



Compute (nova)
==============

Create a keypair::

    from ostack import keypairs
    keypair = keypairs.create('mykey', os.path.expanduser('~/.ssh/id_rsa.pub'))


Image (glance)
==============

List images::

    from ostack import images
    for image in images.list():
        print image.name

Retrive an image by name::

    from ostack import images
    cirros = ostack.images.get(name='cirros')




API reference
=============

.. toctree::
   :maxdepth: 2

   credentials
   endpoints
   images
   instances
   keypairs
   tokens



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

