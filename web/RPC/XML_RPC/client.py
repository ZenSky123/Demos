from xmlrpc.client import ServerProxy

s = ServerProxy("http://localhost:15000", allow_none=True)
s.set('foo', 'bar')
print(s.get('foo'))
