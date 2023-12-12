import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 9999

client.connect( (host, port) )

done = False

while not done:
    message = input('message:').encode('UTF-8')
    client.send(message)

    received_message = client.recv(1024).decode('utf-8')

    if received_message == 'exit':
        done = True
    else:
        print(received_message)