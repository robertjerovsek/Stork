import mock

import stork


class TestApi:
    def test_resource(self):
        api = stork.Api('url')
        resource = api.resource('path')

        assert isinstance(resource, stork.Resource)


class TestResource:
    def test_nested_resource(self):
        r = stork.Resource('path1').resource('path2')

        assert r.path == 'path1/path2'

    def test_nested_resource_slash_beginning(self):
        r = stork.Resource('path1').resource('/path2')
        assert r.path == 'path1/path2'

    def test_nested_resource_slash_end(self):
        r = stork.Resource('path1/').resource('path2')
        assert r.path == 'path1/path2'

    def test_options(self):
        params = {'param1': 'value1', 'param2': 'value2'}
        stork.Resource.client = mock.Mock()
        stork.Resource('path').options(**params)

        stork.Resource.client.request.assert_called_with(
            'options', url='path', params=params)

    def test_get(self):
        params = {'param1': 'value1', 'param2': 'value2'}
        stork.Resource.client = mock.Mock()
        stork.Resource('path').get(**params)

        stork.Resource.client.request.assert_called_with(
            'get', url='path', params=params)

    def test_post(self):
        params = {'param1': 'value1', 'param2': 'value2'}
        data = {'param3': 'value3'}
        stork.Resource.client = mock.Mock()
        stork.Resource('path').post(data=data, **params)

        stork.Resource.client.request.assert_called_with(
            'post', url='path', data=data, params=params)

    def test_put(self):
        params = {'param1': 'value1', 'param2': 'value2'}
        data = {'param3': 'value3'}
        stork.Resource.client = mock.Mock()
        stork.Resource('path').put(data=data, **params)

        stork.Resource.client.request.assert_called_with(
            'put', url='path', data=data, params=params)

    def test_patch(self):
        params = {'param1': 'value1', 'param2': 'value2'}
        data = {'param3': 'value3'}
        stork.Resource.client = mock.Mock()
        stork.Resource('path').patch(data=data, **params)

        stork.Resource.client.request.assert_called_with(
            'patch', url='path', data=data, params=params)

    def test_delete(self):
        params = {'param1': 'value1', 'param2': 'value2'}
        stork.Resource.client = mock.Mock()
        stork.Resource('path').delete(**params)

        stork.Resource.client.request.assert_called_with(
            'delete', url='path', params=params)
