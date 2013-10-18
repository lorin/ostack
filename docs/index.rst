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

List keypairs::

    from ostack import keypairs
    for keypair in keypairs.list():
        print keypair


Image (glance)
==============

List images::

    from ostack import images
    for image in images.list():
        print image.name

Retrive an image by name::

    from ostack import images
    cirros = ostack.images.get(name='cirros')


Specifying credentials explicitly
=================================

By default, *ostack* will look for the following environment variables and
use these as credentials to authenticate against the OpenStack endpoint.

 * ``OS_AUTH_URL``
 * ``OS_USERNAME``
 * ``OS_PASSWORD``
 * ``OS_TENANT_NAME``
 * ``OS_REGION``
 * ``ST_AUTH`` (Swift authentication without keystone)
 * ``ST_USER`` (Swift authentication without keystone)
 * ``ST_KEY`` (Swift authentication without keystone)

You can also explicitly specify authentications with Identity Service
(keystone)::

    from ostack import credentials
    credentials.set(auth_url="http://10.10.0.100:5000/v2.0/",
                    username="admin",
                    password='23jheajsh2$#'
                    tenant_name='acme',
                    region='northeast')

If you are using Object Storage (Swift) with the built-in TempAuth
authentication, specify credentials like this:::

    from ostack import credentials
    credentials.set_swift(auth_url="http://10.10.0.100:8080",
                          user="barney:acme",
                          key="$E&%^rftcuty")



    )



API reference
=============

.. toctree::
   :maxdepth: 2

   account
   containers
   credentials
   endpoints
   images
   instances
   keypairs
   objects
   tokens



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

