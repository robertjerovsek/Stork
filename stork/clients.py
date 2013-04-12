import urllib2

try:
    import urlfetch
except ImportError:
    urlfetch = None


class DefaultClient(object):
    def request(self, method, url, data=None, params=None, headers=None,
                cookies=None, files=None, auth=None, timeout=None,
                allow_redirects=True, verify=False):
        pass


class UrlfetchClient(object):
    def __new__(cls, *args, **kwargs):
        if urlfetch is None:
            raise ImportError('cannot import name urlfetch')
        return object.__new__(cls, *args, **kwargs)

    def request(self, method, url, data=None, params=None, headers=None,
                cookies=None, files=None, auth=None, timeout=None,
                allow_redirects=True, verify=False, allow_truncated=False,
                async=False):
        if headers is None:
            headers = {}
        rpc = urlfetch.create_rpc(deadline=timeout)
        urlfetch.make_fetch_call(
            rpc, url+params, method=method.upper(), payload=data,
            headers=headers, follow_redirects=allow_redirects,
            validate_certificate=verify)

        response = AsyncResponse() if async else rpc.get_result()

        return response
