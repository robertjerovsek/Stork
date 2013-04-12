import collections

from .utils import url_join


class Resource(collections.namedtuple('Resource', 'path')):

    client = None

    def resource(self, path):
        return self.__class__(url_join(self.path, path))

    def request(self, method, **kwargs):
        kwargs['url'] = self.path
        return self.client.request(method, **kwargs)

    def options(self, **params):
        return self.request('options', params=params)

    def get(self, **params):
        return self.request('get', params=params)

    def head(self, **kwargs):
        pass

    def post(self, data=None, **params):
        return self.request('post', data=data, params=params)

    def put(self, data=None, **params):
        return self.request('put', data=data, params=params)

    def patch(self, data=None, **params):
        return self.request('patch', data=data, params=params)

    def delete(self, **params):
        return self.request('delete', params=params)


class Api(object):
    def __init__(self, url):
        self.url = url

    def resource(self, path):
        return Resource(path)
