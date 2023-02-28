import socket

port = 10504

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', port)) #0.0.0.0 todos podem acessar (qualquer ip)
server.listen()


print(f'=== Server aguardando coenxões na porta {port} ===')
conn, addr = server.accept()
print(f'conexão recebida de {addr}')

while True:

    #recebe os dados eviados do cliente
    data = conn.recv(4096)
    fraseC = data.decode()

    print(f'Cliente: {data.decode()}')

    fraseCM = fraseC.upper()
    print(fraseCM)

    conn.send(fraseCM.encode())

#encerra a conexao
conn.close()


