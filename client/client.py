import socket
FORMAT = "UTF8"
# serverAdd = input("Server Add:")
# serverPort = int(input("Server Port:"))

serverAdd='192.168.1.9'
serverPort=65000


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

def login(client):
    username='hoaihcb1'   #input("username:")
    password='phanxuan' #input("password:")
    client.send(username.encode())
    client.recv(1024)

    client.send(password.encode())
    client.recv(1024)

    msg=client.recv(1024).decode()
    client.sendall(msg.encode())
    print(msg)
    

try:
    client.connect((serverAdd, serverPort))

    print("Ket noi thanh cong")

    option = input("TAC VU:")
    if(option=="login"):
        login(client)
    while(1):
        
        msg = input('Client: ')
        client.send(msg.encode(FORMAT))
        msg=client.recv(1024).decode()
        print('Server:',msg)
        if(msg == 'x'):
            break
except:  # Bắt trường hợp server bị đóng
    print("Error")
#.......

client.close()

input()
