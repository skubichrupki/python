import socket
import threading

# specify data to connect
host = input("enter server ip: ")
port = int(input("enter server port: "))

# connect to server
client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client.connect((host, port))

nickname = input('choose a nickname: ')

# get messages
def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'getnickname':
                print('server asks for nickname...')
                client.send(nickname.encode('ascii'))
                print('nickname sent')
            else:
                if (message.split()[0] == nickname):
                    pass
                else:
                    print(message)
        except:
            print('server was shut down')
            client.close()
            break

# send messages
def write():
    while True:
        # prompt, send
        message_input = input("")
        message = f'{nickname} : {message_input}'
        
        # exit message
        if message_input == 'exit':
            print('you have left the chat')
            client.send(f'{nickname} left the chat'.encode('ascii'))
            break
        else:
            client.send(message.encode('ascii'))

# threads
receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()