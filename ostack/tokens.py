from . import credentials


def get():
    """ Retrieve a keystone token """
    return credentials.keystone().auth_token
