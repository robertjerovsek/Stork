import mock

import stork


stork.Resource.client = mock.Mock()


class TestApi:
    def test_resource(self):
        api = stork.Api('http://myapi/v1')
        resource = api.resource('path')

        assert 'http://myapi/v1/path' == resource.path

    def test_default_header(self):
        headers = {'accept-language': 'es'}
        api = stork.Api('http://myapi/v1', headers=headers)
        r = api.resource('path').get()

        stork.Resource.client.request.assert_called_with(
            'get', url='http://myapi/v1/path', params=None, data=None,
            headers=headers, cookies=None, timeout=None, auth=None,
            verify=None, allow_redirects=None)

    def test_default_header_overriden(self):
        headers = {'accept-language': 'es'}
        api = stork.Api('http://myapi/v1', headers=headers)
        r = api.resource('path').get(headers={'accept-language': 'en'})

        stork.Resource.client.request.assert_called_with(
            'get', url='http://myapi/v1/path', params=None, data=None,
            headers=headers, cookies=None, timeout=None, auth=None,
            verify=None, allow_redirects=None)


class TestResource:
    def test_nested_resource(self):
        r = stork.Api('path1').resource('path2')

        assert r.path == 'path1/path2'

    def test_nested_resource_slash_beginning(self):
        r = stork.Api('path1').resource('/path2')
        assert r.path == 'path1/path2'

    def test_nested_resource_slash_end(self):
        r = stork.Api('path1/').resource('path2')
        assert r.path == 'path1/path2'

    def test_options(self):
        stork.Api('path1').resource('path2').options()

        stork.Resource.client.request.assert_called_with(
            'options', url='path1/path2', params=None, data=None,
            headers=None, cookies=None, timeout=None, auth=None,
            verify=None, allow_redirects=None)

    def test_get(self):
        stork.Api('path1').resource('path2').get()

        stork.Resource.client.request.assert_called_with(
            'get', url='path1/path2', params=None, data=None,
            headers=None, cookies=None, timeout=None, auth=None,
            verify=None, allow_redirects=None)

    def test_post(self):
        stork.Api('path1').resource('path2').post()

        stork.Resource.client.request.assert_called_with(
            'post', url='path1/path2', params=None, data=None,
            headers=None, cookies=None, timeout=None, auth=None,
            verify=None, allow_redirects=None)

    def test_put(self):
        stork.Api('path1').resource('path2').put()

        stork.Resource.client.request.assert_called_with(
            'put', url='path1/path2', params=None, data=None,
            headers=None, cookies=None, timeout=None, auth=None,
            verify=None, allow_redirects=None)

    def test_patch(self):
        stork.Api('path1').resource('path2').patch()

        stork.Resource.client.request.assert_called_with(
            'patch', url='path1/path2', params=None, data=None,
            headers=None, cookies=None, timeout=None, auth=None,
            verify=None, allow_redirects=None)

    def test_delete(self):
        stork.Api('path1').resource('path2').delete()

        stork.Resource.client.request.assert_called_with(
            'delete', url='path1/path2', params=None, data=None,
            headers=None, cookies=None, timeout=None, auth=None,
            verify=None, allow_redirects=None)
