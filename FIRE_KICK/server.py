import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 9999
server.bind( (host, port) )

server.listen()
client, address = server.accept()

done = False

while not done:
    message = input("message: ").encode('utf-8')
    client.send(message)

    received_message = client.recv(1024).decode('utf-8')

    if received_message == 'exit':
        done = True
    else:
        print(received_message)

client.close()
server.close()