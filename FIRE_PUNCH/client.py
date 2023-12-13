import socket
import threading

# specify data to connect
host = input("enter server ip: ")
port = int(input("enter server port: "))

# connect to server
client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client.connect((host, port))

nickname = input('choose a nickname: ')
admin_password = input('enter admin password, or just press enter: ')
if admin_password == 'dupsko':
    admin = True
    print('ADMIN RIGHTS UNLOCKED')
else:
    admin = False

print("WELCOME TO")
print("  _____ _____ _____ _____       _____ _____ _____ _____ _____  ")
print(" |   __|     | __  |   __|     |  _  |  |  |   | |     |  |  | ")
print(" |   __|-   -|    -|   __|     |   __|  |  | | | |   --|     | ")
print(" |__|  |_____|__|__|_____|_____|__|  |_____|_|___|_____|__|__| ")
print("                                                               ")

# get messages
def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            # send nickname to the server
            if message == 'getnickname':
                print('server asks for a nickname...')
                client.send(nickname.encode('ascii'))
                print('nickname sent to the server...')
            else:
                # if message is from this client, dont display it
                if (message.split()[0] == nickname):
                    pass
                # if message is from other client, print it
                else:
                    print(message)

        # error handling        
        except:
            print('SERVER WAS SHUT DOWN')
            client.close()
            break

# send messages
def write():
    while True:
        # prompt, send
        message_input = input("")
        message = f'{nickname} : {message_input}'
        
        # exit message - "exit"
        if message_input == 'exit':
            print('you have left the chat')
            break
        # kick message - admin only: "skubi : kick michu"
        elif (admin == True) and (message.split()[2] == 'kick') and (len(message.split()[3]) > 0):
            client.send(f'KICK {message}'.encode('ascii'))
        else:
            client.send(message.encode('ascii'))

# threads
receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()