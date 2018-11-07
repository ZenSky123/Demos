from wsgiref.simple_server import make_server


def simple_application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']


if __name__ == '__main__':
    httpd = make_server('', 8000, simple_application)
    print("Serving HTTP on port 8000...")

    httpd.serve_forever()
