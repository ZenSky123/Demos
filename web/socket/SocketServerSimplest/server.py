from socketserver import TCPServer as TCP, StreamRequestHandler as SRH
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)


class MyRequestHandler(SRH):
    def handle(self):
        print("...connected from :", self.client_address)
        self.wfile.write(bytes('[{}] {}'.format(ctime(), self.rfile.readline()), 'utf-8'))


tcpServ = TCP(ADDR, MyRequestHandler)
print("wating for connection...")
tcpServ.serve_forever()
