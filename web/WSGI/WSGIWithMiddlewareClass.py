from wsgiref.simple_server import make_server
from time import ctime


def simple_application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']


class middleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, *stuff):
        return (bytes('[{}] {}'.format(ctime(), x), 'utf-8') for x in self.app(*stuff))


if __name__ == '__main__':
    httpd = make_server('', 8000, middleware(simple_application))
    print("Serving HTTP on port 8000...")

    httpd.serve_forever()
