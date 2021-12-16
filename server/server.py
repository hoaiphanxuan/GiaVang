from typing import Tuple
import json
import socket
import threading

hostName=socket.gethostname()
hostAdd=socket.gethostbyname(hostName)
print("Host name "+hostName)
print("Host Add "+hostAdd)

# hostPort=int(input('Chon Port muon su dung:'))

hostPort=63220

soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
#Ràng buộc địa chỉ (tên máy chủ, số cổng) vào socket.s
soc.bind((hostAdd,hostPort))
soc.listen(1)

def handleClient(server,clientAdd):
    while(1):
        print("Client Address: ",clientAdd)
        
        msg=server.recv(1024).decode()
        server.sendall(msg.encode())
        res=0
        if(msg=='login'):
            res=login(server)
        elif(msg=='sign up'):
            res=signUp(server)
        elif(msg=="x"):
            pass
        if(res==1 and msg=='login'):
            break;

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

    return checkLogin(server,username,password)

   
def checkLogin(server, username, password):
    with open('account.json',encoding="utf-8") as acc:
        data=json.load(acc)
        for user in data:
            if(user['username']==username ):
                if( user['pass']==password):
                    server.sendall("1".encode())    #ok
                    server.recv(1024)
                    return 1
                else:
                    server.sendall('2'.encode())    #sai mk
                    server.recv(1024)
                    return 2
        server.sendall('3'.encode()) #Khong tim thay tai khoan
        server.recv(1024)
        return 3
                      

def signUp(server):
    username = server.recv(1024).decode()
    server.sendall(username.encode())

    password = server.recv(1024).decode()
    server.sendall(password.encode())

    print("Username: ", username)
    print("Pass:", password)

    return findAndInsertUserToFile(server,username,password)

def findAndInsertUserToFile(server,username,password):
    lisUser=[]
    with open('account.json',mode='r+',encoding="utf-8") as acc:
        data=json.load(acc)
        for user in data:
            if(user['username']==username):
               server.sendall('2'.encode())     #tai khoan da ton tai
               server.recv(1024)
               return 2
            else:
                lisUser.append(user)
        dic={"username":f"{username}","pass":f"{password}"}
        lisUser.insert(0,dic)
    with open('account.json',mode='w',encoding="utf-8") as acc:
        json.dump(lisUser,acc)
    server.sendall('1'.encode())        #tao tai khoan thanh cong
    server.recv(1024)
    return 1

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
