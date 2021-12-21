import socket
import pandas as pd

FORMAT = "UTF8"
# serverAdd = input("Server Add:")
# serverPort = int(input("Server Port:"))

serverAdd='192.168.1.6'
serverPort=63222


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
def sendList(client, list):

    for item in list:
        client.sendall(item.encode(FORMAT))
        #wait response
        client.recv(1024)

    msg = "end"
    client.send(msg.encode(FORMAT))

def recvList(client):
    list = []

    item = client.recv(1024).decode(FORMAT)

    while (item != "end"):
        
        list.append(item)
        #response
        client.sendall(item.encode(FORMAT))
        item = client.recv(1024).decode(FORMAT)
    
    return list
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
    #while(1):
           
        #msg = input('Client: ')
        #client.send(msg.encode(FORMAT))
        #msg=client.recv(1024).decode()    
        #print('Server:',msg)
        #if(msg == 'x'):
            #return
    print("client address:",client.getsockname())
    msg=None
    while(msg!='x'):
        # typee=input("Nhap loai vang: ")
        # area=input("Nhap dia chi: ")
        # day=input("Nhap ngay thang nam(d/m/y): ")
        # listt=[typee,area,day]
        # sendList(client,listt)
        # l=recvList(client)
        # data = [{'type':l[0],'sell':l[1],'buy': l[2],'company': l[3],'brand': l[4],'update':l[5]}]
        # df=pd.DataFrame(data=data)
        # print(df)
        msg=client.recv(4096).decode()
        print(msg)
    
try:
    client.connect((serverAdd, serverPort))
    #client.send('sign up'.encode(FORMAT))
    #msg=client.recv(1024).decode()
    #signUp(client)
    chat(client)
    

except:  # Bắt trường hợp server bị đóng
    print("Error")
#.......

client.close()

input()