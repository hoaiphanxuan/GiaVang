from typing import Tuple
import pyodbc
import socket
import threading

hostName=socket.gethostname()
hostAdd=socket.gethostbyname(hostName)
print("Host name "+hostName)
print("Host Add "+hostAdd)

# hostPort=int(input('Chon Port muon su dung:'))

hostPort=65000

soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
#Ràng buộc địa chỉ (tên máy chủ, số cổng) vào socket.s
soc.bind((hostAdd,hostPort))
soc.listen(1)

def login(server):
    username = server.recv(1024).decode()
    server.sendall(username.encode())

    password = server.recv(1024).decode()
    server.sendall(password.encode())

    print("Username: ", username)
    print("Pass:", password)

    check_Login(server,username,password)
 


def check_Login(server,username, password):
    conn = pyodbc.connect(
        "driver={sql server native client 11.0};"
        "server=laptop-ft73p7ud;"
        "database=Gia_Vang;"
        "trusted_connection=yes;"
    )
    cur=conn.cursor()
    
    temp =findUserForLogIn(cur,username,password)
    if(temp==1):
        server.sendall("Dang nhap thanh cong".encode())
        server.recv(1024)
    elif(temp==0):
        server.sendall('Khong tim thay tai khoan'.encode())
        server.recv(1024)
    else:
        server.sendall('Mat khau khong dung'.encode())
        server.recv(1024)
        
       
def findUserForLogIn(cur,username,password):
    cur.execute("select pass from  Account where username=?",username)
    for temp in cur:
        print(temp)
        str = temp[0]
        
        if(str==password):
            return 1
        elif(temp==''):
            return 0
        else:
            return -1       

def signUp(server):
    username = server.recv(1024).decode()
    server.sendall(username.encode())

    password = server.recv(1024).decode()
    server.sendall(password.encode())

    print("Username: ", username)
    print("Pass:", password)

    findAndInsertUserToSQL(server,username,password)

def findAndInsertUserToSQL(server,username,password):
    conn = pyodbc.connect(
        "driver={sql server native client 11.0};"
        "server=laptop-ft73p7ud;"
        "database=Gia_Vang;"
        "trusted_connection=yes;"
    )
    cur=conn.cursor()
    cur.execute("select pass from Account where username=?",username)
    temp=cur.fetchone()
    if(temp==None):
        cur.execute('insert into Account(username,pass) Values(?,?);',(username,password))
        conn.commit()
        conn.close()

        server.sendall('Dang ky thanh cong'.encode())
        server.recv(1024)
    else:
        server.sendall('Tai khoan da ton tai'.encode())
        server.recv(1024)

def chat(server):
    while 1:
        msg=server.recv(1024).decode()
        print("Client: "+msg)

        if(msg=='x'):
            return

        msg = input("Server:")
        server.sendall(msg.encode())
           
        
       
 

try:
    server, clientAdd =soc.accept()
    print("Client Address: ",clientAdd)
    
    msg=server.recv(1024).decode()
    server.sendall(msg.encode())

    if(msg=='login'):
        login(server)
    elif(msg=='sign up'):
        signUp(server)
    elif(msg=="x"):
        pass
    else:
        chat(server)
    chat(server)
    
        
            
        
except: #Bắt trường hợp client đóng kết nối đột ngột
    print("Error")
#.
server.close()
