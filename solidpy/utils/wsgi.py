# `get_headers` comes from `werkzeug.datastructures.EnvironHeaders`
def get_headers(environ):
    """
    Returns only proper HTTP headers.
    """
    for key, value in environ.iteritems():
        key = str(key)
        if key.startswith('HTTP_') and key not in \
           ('HTTP_CONTENT_TYPE', 'HTTP_CONTENT_LENGTH'):
            yield key[5:].replace('_', '-').title(), value
        elif key in ('CONTENT_TYPE', 'CONTENT_LENGTH'):
            yield key.replace('_', '-').title(), value


def get_environ(environ):
    """
    Returns our whitelisted environment variables.
    """
    for key in ('REMOTE_ADDR', 'SERVER_NAME', 'SERVER_PORT'):
        if key in environ:
            yield key, environ[key]


# `get_host` comes from `werkzeug.wsgi`
def get_host(environ):
    """Return the real host for the given WSGI environment.  This takes care
    of the `X-Forwarded-Host` header.

    :param environ: the WSGI environment to get the host of.
    """
    scheme = environ.get('wsgi.url_scheme')
    if 'HTTP_X_FORWARDED_HOST' in environ:
        result = environ['HTTP_X_FORWARDED_HOST']
    elif 'HTTP_HOST' in environ:
        result = environ['HTTP_HOST']
    else:
        result = environ['SERVER_NAME']
        if (scheme, str(environ['SERVER_PORT'])) not \
           in (('https', '443'), ('http', '80')):
            result += ':' + environ['SERVER_PORT']
    if result.endswith(':80') and scheme == 'http':
        result = result[:-3]
    elif result.endswith(':443') and scheme == 'https':
        result = result[:-4]
    return result

