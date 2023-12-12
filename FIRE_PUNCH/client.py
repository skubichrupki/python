import socket
import threading

# server is listening all the time,
# the client is choosing a nickname
# connects to the server,
# server sends keyword NICK

nickname = input('sys_cmd: choose a nickname: ')

client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client.connect(('localhost', 55554))


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                pass
            else:
                # if string from beginning = my nickname dont show it (to do)
                print(message)
        except:
            print('error')
            client.close()
            break

def write():
    while True:
        # prompclst for message from client
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()