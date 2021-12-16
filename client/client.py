import socket
FORMAT = "UTF8"

# serverAdd = input("Server Add:")
# serverPort = int(input("Server Port:"))

serverAdd='192.168.1.6'
serverPort=63220


global client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

def login(username,password):
    client.sendall('login'.encode())
    client.recv(1024)
    if(username == '' or password ==''):
        print('Tai khoan va mat khau khong duoc de trong')
        return '0'

    client.send(username.encode())
    client.recv(1024)

    client.send(password.encode())
    client.recv(1024)

    msg=client.recv(1024).decode()
    client.sendall(msg.encode())
    print(msg)
    return msg
    
def signUp(username,password):
    client.sendall('sign up'.encode())
    client.recv(1024)
    # username=input('Username:')
    # password=input('Password:')

    if(username == '' or password ==''):
        print('Tai khoan va mat khau khong duoc de trong')
        return '0'
    
    client.send(username.encode())
    client.recv(1024)

    client.send(password.encode())
    client.recv(1024)

    msg=client.recv(1024).decode()
    client.sendall(msg.encode())
    print(msg)
    return msg

def chat(client):
    while(1):
            
        msg = input('Client: ')
        client.send(msg.encode(FORMAT))
        msg=client.recv(1024).decode()
        
        print('Server:',msg)
        if(msg == 'x'):
            return

#.......



