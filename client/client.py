import socket
FORMAT = "UTF8"
# serverAdd = input("Server Add:")
# serverPort = int(input("Server Port:"))

serverAdd='192.168.255.1'
serverPort=65000


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

def login(client):
    while True:
        username='hoaihcb1'   #input("username:")
        password='phanxuan' #input("password:")
        if(username != '' and password !=''):
            break
        else:
            print('Tai khoan va mat khau khong duoc de trong')

    client.send(username.encode())
    client.recv(1024)

    client.send(password.encode())
    client.recv(1024)

    msg=client.recv(1024).decode()
    client.sendall(msg.encode())
    print(msg)
    
def signUp(client):
    username=input('Username:')
    password=input('Password:')

    while True:
        if(username != '' and password !=''):
            break
        else:
            print('Tai khoan va mat khau khong duoc de trong')
    
    client.send(username.encode())
    client.recv(1024)

    client.send(password.encode())
    client.recv(1024)

    msg=client.recv(1024).decode()
    client.sendall(msg.encode())
    print(msg)

def chat(client):
    while(1):
            
            msg = input('Client: ')
            client.send(msg.encode(FORMAT))
            msg=client.recv(1024).decode()
            
            print('Server:',msg)
            if(msg == 'x'):
                return

try:
    client.connect((serverAdd, serverPort))

    print("Ket noi thanh cong")

except:  # Bắt trường hợp server bị đóng
    print("Error")
#.......

client.close()

input()
