from threading import Thread
from time import sleep
import socket

port = 10500





class Threadserver(Thread):
    def __init__(self, conn, addr):
        Thread.__init__(self)
        self.conn = conn
        self.addr = addr

    def run(self):
        data = self.conn.recv(4096)

        fraseC = data.decode()

        print(f'Cliente: {data.decode()}')

            
        frasee = fraseC.split()

        print(frasee)

        if frasee[1] == '+':
            calculo = int(frasee[0]) + int(frasee[2])
        if frasee[1] == '-':
            calculo = int(frasee[0]) - int(frasee[2])
        if frasee[1] == '*':
            calculo = int(frasee[0]) * int(frasee[2])
        if frasee[1] == '/':
            calculo = int(frasee[0]) / int(frasee[2])
        



        print(calculo)

        calculostr = str(calculo)
        #envia string
        self.conn.send(calculostr.encode())


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', port))
    server.listen()

    while True:

        print(f'=== Server aguardando coenxões ===')
        conn, addr = server.accept()
        Threadserver(conn, addr).start()









if __name__ == '__main__':
    main()



