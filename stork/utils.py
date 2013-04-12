import posixpath
import urlparse


def url_join(*paths):
    """Join an arbitrary number of url segments together."""
    if not paths:
        return ''
    scheme, netloc, path, query, fragment = urlparse.urlsplit(paths[0])
    # path = posixpath.join(path, *[('%s' % path) for path in paths[1:]])
    path = '/'.join(p.strip('/') for p in (path,) + paths[1:])

    return urlparse.urlunsplit([scheme, netloc, path, query, fragment])
