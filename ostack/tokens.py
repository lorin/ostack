from . import credentials


def get():
    """ Retrieve the keystone token """
    return credentials.keystone().auth_token
