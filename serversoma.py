import socket

port = 10509

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#0.0.0.0 todos podem acessar
server.bind(('0.0.0.0', port))
server.listen()


print(f'=== Server aguardando coenxões na porta {port} ===')
conn, addr = server.accept() #enquanto não tiver conexão codigo trava aqui
print(f'conexão recebida de {addr}')

while True:

        #recebe os dados eviados do cliente
    data = conn.recv(4096)
    #recebe como string
    fraseC = data.decode()

    print(f'Cliente: {data.decode()}')

    operacao = fraseC[2]

    calculo = int(fraseC[0]) + int(fraseC[4])

    print(calculo)

    calculostr = str(calculo)
    #envia string
    conn.send(calculostr.encode())



    #encerra a conexao
conn.close()

