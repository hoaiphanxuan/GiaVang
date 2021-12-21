from typing import Tuple
import json
import socket
import requests, json
import os
from bs4 import BeautifulSoup
from datetime import date
import threading
import time, traceback
import time
from datetime import datetime
FORMAT = "UTF8"
hostName=socket.gethostname()
hostAdd=socket.gethostbyname(hostName)
print("Host name "+hostName)
print("Host Add "+hostAdd)

# hostPort=int(input('Chon Port muon su dung:'))

hostPort=63210

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
    
def updateDataEvery30Min():
  delay=int(1800)	
  next_time = time.time() + delay
  while True:
    time.sleep(max(0, next_time - time.time()))
    try:
        today=date.today()
        checkExistFile(today.strftime("%Y%m%d"))
    except Exception:
        traceback.print_exc()   
    next_time += (time.time() - next_time) // delay * delay + delay

def chat(server):
    msg=None
    while(msg != 'x'):
        l=recvList(server)
        listt, c = Search(l[0],l[1],convert(l[2]))
        server.send(str(c).encode('utf-8'))
        print(c)
        for i in range (c):
            sendList(server,listt[i])

def sendList(server, list):
    for item in list:
        server.sendall(item.encode('utf-8'))
        #wait response
        server.recv(1024)
    msg = "end"
    server.send(msg.encode('utf-8'))           
  
def recvList(server):
    list = []
    item = server.recv(1024).decode(FORMAT)
    while (item != "end"):  
        list.append(item)
        #response
        server.sendall(item.encode(FORMAT))
        item = server.recv(1024).decode(FORMAT)
    
    return list

def getDataFromWeb(date):
    response = requests.get("https://tygia.com/json.php?ran=0&rate=0&gold=1&bank=VIETCOM&date="+date)
    #soup = BeautifulSoup(response.content, "html.parser")

    data = response.content.decode('UTF-8-sig')
    #data kiểu là string
    #chuyển kiểu dữ liệu của data từ string sang dict (có cấu trúc tương tự json)
    js=json.loads(data)

    #sử dụng phương thức get() của dict lấy ra các giá trị của golds =>js1 lúc này có kiểu list
    js1=js.get('golds')

    #js1[0] => lấy phần đầu của danh sách; js1[0] có kiểu dict =>js1[0].get('value') có kiểu list 
    js2 = js1[0].get('value')
    return js2

def checkExistFile(date):
    dataWeb=getDataFromWeb(date)
    with open('data.json',mode='w',encoding='UTF-8') as file:
        json.dump(dataWeb,file)

def Search(type,area,date):
    checkExistFile(date)
    with open('data.json',mode='r',encoding='UTF-8') as data:
        getdata=json.load(data)
        l=[]
        c=0
        if(area=='Tất cả'): 
            for i in range(len(getdata)):
                if((getdata[i]['type']==type) & (getdata[i]['day']==date)):
                    listt=[getdata[i]['type'],getdata[i]['sell'],getdata[i]['buy'],getdata[i]['company'],getdata[i]['brand'],getdata[i]['updated']]
                    c=c+1
                    l.append(listt)
        else:
            for i in range(len(getdata)):
                if((getdata[i]['type']==type) & (getdata[i]['day']==date) & (getdata[i]['brand']==area)):
                    listt=[getdata[i]['type'],getdata[i]['sell'],getdata[i]['buy'],getdata[i]['company'],getdata[i]['brand'],getdata[i]['updated']]
                    c=c+1
                    l.append(listt)

        return l, c
    listt=[" "," "," "," "," "," "]
    return listt

def convert(date):
    date_object = datetime.strptime(date, "%d/%m/%Y")
    a=date_object.year*10000+date_object.month*100+date_object.day
    return str(a)

def handleClient(server,clientAdd):
    print("Client Address: ",clientAdd)
    chat(server)
    print("Client :",clientAdd , "end.")
    soc.close()
    
nClient = 0
while(nClient<10):       
    try:
        server, clientAdd =soc.accept()
        #threading.Thread(target=lambda: updateDataEvery30Min()).start()
        handleClient(server,clientAdd)
        thr = threading.Thread(target=handleClient, args=(server,clientAdd))
        thr.daemon = False
        thr.start()
    except: #Bắt trường hợp client đóng kết nối đột ngột
        print("Error")
    nClient+=1

print("End server")

soc.close()