import threading
import socket
import os
from dotenv import load_dotenv

load_dotenv()

# specify data to set up server
host = input("set up server ip: ")
port = int(input("set up server port: "))
# host = os.getenv('HOST')
# port = int(os.getenv('PORT'))
server_name = input("set up the server name: ")

 # af_inet = ipv4, sock_stream = tcp
server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# lists for clients and their nicknames
clients = []
nicknames = []

# broadcast function -> send message for ever client connected to the server 
def broadcast(message):
    for client in clients:
        client.send(message)

# handle the client connection
def handle(client):
    while True:
        # get message, broadcast it
        try:
            message = client.recv(1024)

            # kick functionality
            if message.startswith(b'KICK'):
                print('kick request recvd on the server, but nobody was kicked out because dev is a lazy fuck')
            else:
                broadcast(message)

        # when client exit
        except:
            # remove client, close connection
            index = clients.index(client)
            clients.remove(client)
            client.close()

            # remove the nickname
            nickname = nicknames[index]
            nicknames.remove(nickname)
            broadcast(f"{nickname} left the chat".encode('ascii'))
            break

# handle client connection
def receive():
    while True:
        # accept clients all the time, when connected print message
        client, address = server.accept()
        print(f"connected with {str(address)}")

        # send keyword getnickname, receive nickname, append nickname and client to lists
        client.send('getnickname'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)
        client.send(f'success, welcome to {server_name}, {nickname}'.encode('ascii'))

        print(f'clients on the server: {nicknames}')
        broadcast(f'{nickname} joined {server_name}'.encode('ascii'))
        broadcast(f'currently on the server: {nicknames}'.encode('ascii'))

        # one thread for each client to process at the same time
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print(f'server {server_name} is listening on {host}:{port} :]')
receive()