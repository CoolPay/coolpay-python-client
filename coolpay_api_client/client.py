import base64
import json
from functools import partial

from .api import CPApi


class CPClient(object):
    METHODS = ['get', 'post', 'put', 'patch', 'delete']

    def __init__(self, *args):
        self.api = CPApi(*args)

    def __getattr__(self, method):
        if method in self.METHODS:
            return partial(getattr(self.api, 'perform'), method)
        else:
            raise AttributeError('unsupported http method: %s' % method)
