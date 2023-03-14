from threading import Thread
from time import sleep
import socket

port = 10501
adress = '0.0.0.0'

acessos = 0

def handle_http_request(request):
    print(request)

def handle_http_response():
    response = f'''
HTTP/1.0 200 OK
Date: tue, 14 Mar 2023 15:11:00 GMT-3
Server: AulaRedes/1.0
Content-Type: text/HTML

<html>
    <head>
        <title>
        Aula
        </title>
    </head>
    <body>
        <h1>Aula de redes</h1>
        <h2> alguma coisa</h2>
        Este servidor foi acessado {acessos} vezes.
        <a href="http://falecenciabet.lovestoblog.com/?i=1">site de apostas</a> 
    </body>
</html>
'''
    return response



class Threadserver(Thread):
    def __init__(self, conn, addr):
        Thread.__init__(self)
        self.conn = conn
        self.addr = addr

    def run(self):
        data = self.conn.recv(4096)

        msg_recv = data.decode()
        msg_env = 'data alguma coisa'

        print(f'Cliente: {data.decode()}')

            
        # frasee = fraseC.split()

        # print(frasee)

        # if frasee[1] == '+':
        #     calculo = int(frasee[0]) + int(frasee[2])
        # if frasee[1] == '-':
        #     calculo = int(frasee[0]) - int(frasee[2])
        # if frasee[1] == '*':
        #     calculo = int(frasee[0]) * int(frasee[2])
        # if frasee[1] == '/':
        #     calculo = int(frasee[0]) / int(frasee[2])
        # print(calculo)
        # calculostr = str(calculo)
        # #envia string
        # self.conn.send(calculostr.encode())

        self.conn.send(handle_http_response().encode())
        


        


def main():
    global acessos
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((adress, port))
    server.listen()

    while True:

        print(f'=== Server aguardando coenxões ===')
        acessos += 1
        conn, addr = server.accept()
        Threadserver(conn, addr).start()



if __name__ == '__main__':
    main()



