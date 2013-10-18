'''

OpenStack keypairs


'''
import os.path

from .credentials import nova



def list():
    """ Return a list of keypairs """
    return nova().keypairs.list()


def create(name, keyfile=None):
    """ Create a named keypair from an SSH public key file

    name : str
        Name of the keypair
    keyfile : str
        Path to the public key file. If *None*, will default to
        :file:`~/.ssh/id_rsa.pub`

    """
    if keyfile is None:
        keyfile = os.path.expanduser('~/.ssh/id_rsa.pub')
    with open(keyfile) as fpubkey:
       nova().keypairs.create(name=name, public_key=fpubkey.read())

