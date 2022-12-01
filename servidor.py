import threading
import socket

host = '127.0.0.1'
port = 55555

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((host, port))
servidor.listen()

clientes = []
nicknames = []

def broadcast(message):
    for cliente in clientes:
        cliente.send(message)

def handle(cliente):
    while True:
        try:
            message = cliente.recv(1024)
            broadcast(message)
        except:
            index = clientes.index(cliente)
            clientes.remove(cliente)
            cliente.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} saiu do chat!'.encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        cliente, address = servidor.accept()
        print(f'Conectado com {str(address)}')

        cliente.send('NOME'.encode('ascii'))
        nickname = cliente.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clientes.append(cliente)

        print(f'O nome do clientee eh {nickname}!')
        broadcast(f'{nickname} entrou no chat!'.encode('ascii'))
        cliente.send('Conectado no servidor!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(cliente,))
        thread.start()

print('Servidor está online...')
receive()
