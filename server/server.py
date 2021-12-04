from typing import Tuple
import json
import socket
import threading

hostName=socket.gethostname()
hostAdd=socket.gethostbyname(hostName)
print("Host name "+hostName)
print("Host Add "+hostAdd)

# hostPort=int(input('Chon Port muon su dung:'))

hostPort=63213

soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
#Ràng buộc địa chỉ (tên máy chủ, số cổng) vào socket.s
soc.bind((hostAdd,hostPort))
soc.listen(1)

def handleClient(server,clientAdd):
    print("Client Address: ",clientAdd)
    
    msg=server.recv(1024).decode()
    server.sendall(msg.encode())

    if(msg=='login'):
        login(server)
    elif(msg=='sign up'):
        signUp(server)
    elif(msg=="x"):
        pass
    chat(server)
    print("Client :",clientAdd , "end.")
    soc.close()
def login(server):
    username = server.recv(1024).decode()
    server.sendall(username.encode())

    password = server.recv(1024).decode()
    server.sendall(password.encode())

    print("Username: ", username)
    print("Pass:", password)

    checkLogin(server,username,password)

   
def checkLogin(server, username, password):
    with open('account.json',encoding="utf-8") as acc:
        data=json.load(acc)
        for user in data:
            if(user['username']==username and user['pass']==password):
                server.sendall("Dang nhap thanh cong".encode())
                server.recv(1024)
            elif(user['username']==username):
                server.sendall('Mat khau khong dung'.encode())
                server.recv(1024)
            else:
                server.sendall('Khong tim thay tai khoan'.encode())
                server.recv(1024)
                      

def signUp(server):
    username = server.recv(1024).decode()
    server.sendall(username.encode())

    password = server.recv(1024).decode()
    server.sendall(password.encode())

    print("Username: ", username)
    print("Pass:", password)

    findAndInsertUserToFile(server,username,password)

def findAndInsertUserToFile(server,username,password):
    lisUser=[]
    with open('account.json',mode='r+',encoding="utf-8") as acc:
        data=json.load(acc)
        for user in data:
            if(user['username']==username):
               server.sendall('Tài khoản đã tồn tại'.encode())
               server.recv(1024)
               return 0
            else:
                lisUser.append(user)
        dic={"username":f"{username}","pass":f"{password}"}
        lisUser.insert(0,dic)
    with open('account.json',mode='w',encoding="utf-8") as acc:
        json.dump(lisUser,acc)
    server.sendall('Đăng ký tài khoản thành công'.encode())
    server.recv(1024)

def chat(server):
    while (1):
        msg=server.recv(1024).decode()
        print("Client: "+msg)

        if(msg=='x'):
            return
        msg = input("Server:")
        server.sendall(msg.encode())
           
        
nClient = 0
while(nClient<10):       
    try:
        server, clientAdd =soc.accept()
        handleClient(server,clientAdd)
        thr = threading.Thread(target=handleClient, args=(server,clientAdd))
        thr.daemon = False
        thr.start()

        quit=input()
        if(quit=='x'):
            break
            
    except: #Bắt trường hợp client đóng kết nối đột ngột
        print("Error")
        soc.close()

    nClient+=1

print("End server")

soc.close()
