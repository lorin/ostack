'''

Calls that are a specific to the active OpenStack-related account


'''
import uuid

from .credentials import swift


def get_temp_url_key():
    """ Retrieve the secret key used to sign Swift temporary urls

    Raises KeyError if the key isn't set"""
    account = swift().get_account()
    return account[0]['x-account-meta-temp-url-key']


def set_temp_url_key(key=str(uuid.uuid4())):
    """ Set the secret key used to sign Swift

    If not specified, it will set a random uuid as the key """
    swift().post_account({'X-Account-Meta-Temp-URL-Key': key})
    return key
