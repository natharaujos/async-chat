import socket
import threading

apelido = input("Escolha um apelido: ")

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('127.0.0.1', 55555))

def receive():
    while True:
        try:
            mensagem = cliente.recv(1024).decode('ascii')
            if mensagem == 'NOME':
                cliente.send(apelido.encode('ascii'))
            else:
                print(mensagem)
        except:
            print('Um erro ocorreu!')
            cliente.close()
            break

def write():
    while True:
        mensagem = f'{apelido}: {input("")}'
        cliente.send(mensagem.encode('ascii'))

receiveThread = threading.Thread(target=receive)
receiveThread.start()

writeThread = threading.Thread(target=write)
writeThread.start()
