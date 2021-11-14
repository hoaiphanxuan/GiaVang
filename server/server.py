import pyodbc
import socket
import threading

hostName=socket.gethostname()
hostAdd=socket.gethostbyname(hostName)
print("Host name "+hostName)
print("Host Add "+hostAdd)

hostPort=int(input('Chon Port muon su dung:'))


soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
#Ràng buộc địa chỉ (tên máy chủ, số cổng) vào socket.s
soc.bind((hostAdd,hostPort))
soc.listen(1)


try:
    clientConnection, clientAdd =soc.accept()
    print("Client Address: ",clientAdd)
   
    while(1):
        msg=input("username:")
        msg2=input("password:")
        clientConnection.send(msg.encode())
        clientConnection.send(msg2.encode())
        msg=clientConnection.recv(1024).decode()
        print("Client: "+msg)

        if(msg=="x"):
            break
except: #Bắt trường hợp client đóng kết nối đột ngột
    print("Error")

clientConnection.close()