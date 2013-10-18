from .credentials import swift


def list():
    """ Return a list of Swift containers """
    return swift().get_account(full_listing=True)[1]
