import threading
import socket

# TCP - Transmission Control Protocol

# define server/machine localhost address
# The host variable is set to '127.0.0.1', which is the standard IP address for localhost.
host = 'localhost'
port = 55554

 # af_inet -> ipv4, sock_stream -> tcp
server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind( (host, port))
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
        # on received message -> broadcast the message to clients
        try:
            message = client.recv(1024)
            broadcast(message)
        # on error (disconnecting) -> remove client from the list, remove the nickname, broadcast that client left
        except:
            # index = clients[3] or so index = 3
            index = clients.index(client)
            clients.remove(client)
            client.close()
            #also remove the nickname
            nickname = nicknames[index]
            nicknames.remove(nickname)
            broadcast(f"sys_broadcast: {nickname} left the chat".encode('ascii'))
            break

# handle client connection
def receive():
    while True:
        # accept clients all the time, when connected print message
        client, address = server.accept()
        print("sys_cmd: connected with {}".format(str(address)))

        # send keyword nick, receive nickname, append nickname and client to lists
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)
        print(f'clients on the server: {nicknames}')

        # success -> print nickname message, broadcast to chat, send message to client
        print(f'sys_cmd: nickname of client: {format(nickname)}')
        broadcast(f'sys_broadcast: {format(nickname)} joined the chat'.encode('ascii'))
        client.send('sys_clientsend: connected to the server'.encode('ascii'))

        # one thread for each client to process at the same time
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print('sys_cmd: server is listening..')
receive()