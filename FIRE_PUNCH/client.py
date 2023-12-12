import socket
import threading

# server is listening all the time,
# the client is choosing a nickname
# connects to the server,
# server sends keyword NICK

nickname = input('sys_cmd: choose a nickname: ')

client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55554))


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                pass
            else:
                print(message)
        except:
            print('error')
            client.close()
            break

def write():
    while True:
        # prompt for message from client
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()