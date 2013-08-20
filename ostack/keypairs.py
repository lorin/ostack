from .credentials import nova

def list():
    """ List keypairs """
    return nova.keypairs.list()
