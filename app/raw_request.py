from urllib import quote

def adaptHeader(txt):
    """Input: string, header name as it is in web.ctx.env
    Output: string, header name according to http protocol.
    es: "HTTP_CACHE_CONTROL" => "Cache-Control"
    """
    txt = txt.replace('HTTP_', '')
    return '-'.join((t[0] + t[1:].lower() for t in txt.split('_')))

def rawRequest(env):
    """Reconstruct and return the web request based on web.ctx.env"""

    # url reconstruction
    # see http://www.python.org/dev/peps/pep-0333/#url-reconstruction
    url = env['wsgi.url_scheme']+'://' # http/https
    url += env.get('HTTP_HOST') or (env['SERVER_NAME']+':'+env['SERVER_PORT']) # host + port
    url += quote(env.get('SCRIPT_NAME', ''))
    url += quote(env.get('PATH_INFO', ''))
    url += ('?' + env['QUERY_STRING']) if env.get('QUERY_STRING') else '' # GET querystring

    # get/post request
    req = ' '.join((env['REQUEST_METHOD'], url, env['SERVER_PROTOCOL'])) + '\n'

    # headers
    for k, v in env.items():
        if k.startswith('HTTP') or k in ('CONTENT_TYPE', 'CONTENT_LENGTH'):
          req += adaptHeader(k) + ': ' + str(v) + '\n'

    # post data 
    try:
        req += '\n' + env['wsgi.input'].read(int(env['CONTENT_LENGTH']))
    except:
        pass

    return req