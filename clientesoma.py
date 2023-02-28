import socket

port = 10509

dest = '192.168.246.46'
#local da conexão

msg = 'simm'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(f'=== conectando ao servidor {dest}:{port}')
client.connect((dest, port))

while True:

    msg = str(input(': '))
    #envia string para o servidor conectado
    client.send(msg.encode())

    #recebe os dados eviados do server
    data = client.recv(4096)
    print(f'servidor: {data.decode()}')

#fecha a conexão
client.close()
