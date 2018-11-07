from wsgiref.simple_server import make_server
from time import ctime


def simple_application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']


def middleware(environ, start_response):
    return (bytes('[{}] {}'.format(ctime(), x), 'utf-8') for x in simple_application(environ, start_response))


if __name__ == '__main__':
    httpd = make_server('', 8000, middleware)
    print("Serving HTTP on port 8000...")

    httpd.serve_forever()
