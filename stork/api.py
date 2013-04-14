from collections import namedtuple

from .utils import url_join
from .serializers import Json


class Resource(namedtuple('Resource', ('path headers timeout auth'))):

    __slots__ = ()
    client = None

    def resource(self, path):
        return self.__class__(url_join(self.path, path), headers=self.headers,
                              timeout=self.timeout, auth=self.auth)

    def request(self, method, params=None, data=None, headers={},
                cookies=None, files=None, auth=None, timeout=None, verify=None,
                allow_redirects=None):
        """Send a request.

        :param method: Request method.
        :param params: Dictionary or bytes to be sent in the query string.
        :param headers: Dictionary of HTTP Headers to send with the request.
        :param cookies: Dict or CookieJar object to send with the request.
        :param auth: Auth tuple to enable Basic/Digest/Custom HTTP Auth.
        :param timeout: Float describing the timeout of the request.
        :param allow_redirects: Boolean. Set to True if POST/PUT/DELETE
            redirect following is allowed.
        :param verify: If ``True``, the SSL cert will be verified.

        :return: :class:`Response <Response>` object.
        """
        if self.headers is not None:
            default_headers = self.headers.copy()
            default_headers.update(headers)
            headers = default_headers
        if timeout is None:
            timeout = self.timeout
        if auth is None:
            auth = self.auth
        return self.client.request(method, url=self.path, params=params,
                                   data=data, headers=headers, cookies=cookies,
                                   timeout=timeout, auth=auth, verify=verify,
                                   allow_redirects=allow_redirects)

    def options(self, **kwargs):
        return self.request('options', **kwargs)

    def get(self, **kwargs):
        return self.request('get', **kwargs)

    def head(self, **kwargs):
        pass

    def post(self, **kwargs):
        return self.request('post', **kwargs)

    def put(self, **kwargs):
        return self.request('put', **kwargs)

    def patch(self, **kwargs):
        return self.request('patch', **kwargs)

    def delete(self, **kwargs):
        return self.request('delete', **kwargs)


class Api(object):
    """Base object from which build the resources.

    Initialization params:
        `api_url`
            Base api url. Ex: ``http://api.myapp.com/v1``

        `headers`
            Dictionary of default HTTP Headers to send always in the request.

        `auth`
            Default auth tuple to enable Basic/Digest/Custom HTTP Auth.

        `timeout`
            Default timeout as a ``float`` to use when sending the request.
    """
    def __init__(self, api_url, headers=None, cookies=None, timeout=None,
                 auth=None):
        self.api_url = api_url
        self.base_resource = Resource(api_url, headers=headers, timeout=timeout,
                                      auth=auth)

    def resource(self, path):
        return self.base_resource.resource(path)
