from stork.utils import url_join


def test_urlparse_simple():
    assert 'path' == url_join('path')


def test_urlparse_several():
    assert 'path1/path2' == url_join('path1', 'path2')


def test_urlparse_base_and_path():
    assert 'http://my.web/path' == url_join('http://my.web', 'path')


def test_urlparse_base():
    assert 'http://my.web' == url_join('http://my.web')
