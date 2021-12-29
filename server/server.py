from typing import Tuple
import json
import socket
import requests, json
import os
from datetime import date
import threading
import time, traceback
import time
from datetime import datetime
FORMAT = "UTF8"
##lib gui
from pathlib import Path
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk

hostName=socket.gethostname()
hostAdd=socket.gethostbyname(hostName)
print("Host name "+hostName)
print("Host Add "+hostAdd)

# hostPort=int(input('Chon Port muon su dung:'))

hostPort=63215
global soc
soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#Ràng buộc địa chỉ (tên máy chủ, số cổng) vào socket.s
soc.bind((hostAdd,hostPort))
soc.listen()

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

def updateDataEvery30Min():
  delay=int(1800)	
  next_time = time.time() + delay
  while True:
    global stopThread1
    if stopThread1:
        break
    time.sleep(max(0, next_time - time.time()))
    try:
        today=date.today()
        checkExistFile(today.strftime("%Y%m%d"))
    except Exception:
        traceback.print_exc()   
    next_time += (time.time() - next_time) // delay * delay + delay

def chat(server,clientAdd):
    try:
        while(1):
            msg=server.recv(1024).decode()
            server.sendall(msg.encode())
            res=0
            if(msg=='login'):
                res=login(server)
            elif(msg=='sign up'):
                res=signUp(server)
            elif(msg=="xxx"):
                #server.shutdown(socket.SHUT_RDWR)
                pass
            if(res==1 and msg=='login'):
                break

        msg=None
        while(msg != 'xxx'):
            l,msg=recvList(server)
            if(msg=="xxx"):
                break
            # temp=convert(l[2])
            # print(temp)
            listt, c = Search(l[0],l[1],l[2])
            print(listt)
            server.send(str(c).encode('utf-8'))
            #print(c)
            for i in range (c):
                sendList(server,listt[i])
    except Exception as s:
        print(s)

def sendList(server, list):
    for item in list:
        if(item==""):
            item="null"
        server.sendall(item.encode('utf-8'))
        #wait response
        server.recv(1024)
    msg = "end"
    server.send(msg.encode('utf-8'))
    server.recv(1024)          
  
def recvList(server):
    list = []
    item = server.recv(1024).decode(FORMAT)
    if(item=="xxx"):
        print(clientAdd,'disconnect')
        #server.shutdown(socket.SHUT_RDWR)
        return list,item
    while (item != "end"):
        print(item)  
        list.append(item)
        #response
        server.sendall(item.encode(FORMAT))
        item = server.recv(1024).decode(FORMAT)
 
    print(list)
    return list,item

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

def Search(type,area,dat):
    print(type,area, dat)
    checkExistFile(dat)
    with open('data.json',mode='r',encoding='UTF-8') as data:
        getdata=json.load(data)
        l=[]
        c=0

        if(area=="Tất cả"):
            if(type=="Tất cả"):
                for i in range(len(getdata)):
                    if(getdata[i]['day']==dat):
                        listt=[getdata[i]['type'],getdata[i]['sell'],getdata[i]['buy'],getdata[i]['company'],getdata[i]['brand'],getdata[i]['updated']]
                        print(listt)
                        c=c+1
                        l.append(listt)
            else:
                for i in range(len(getdata)):
                    if((getdata[i]['type']==type) and (getdata[i]['day']==dat)):
                        listt=[getdata[i]['type'],getdata[i]['sell'],getdata[i]['buy'],getdata[i]['company'],getdata[i]['brand'],getdata[i]['updated']]
                        c=c+1
                        l.append(listt)
        else:
            if(type=="Tất cả"):
                for i in range(len(getdata)):
                    if((getdata[i]['brand']==area) and (getdata[i]['day']==dat)):
                        listt=[getdata[i]['type'],getdata[i]['sell'],getdata[i]['buy'],getdata[i]['company'],getdata[i]['brand'],getdata[i]['updated']]
                        c=c+1
                        l.append(listt)
            else:
                for i in range(len(getdata)):
                    if((getdata[i]['type']==type) and (getdata[i]['day']==dat) and (getdata[i]['brand']==area)):
                        listt=[getdata[i]['type'],getdata[i]['sell'],getdata[i]['buy'],getdata[i]['company'],getdata[i]['brand'],getdata[i]['updated']]
                        c=c+1
                        l.append(listt)

        return l, c
    listt=[" "," "," "," "," "," "]
    return listt


global count
count=0

def handleClient(server,clientAdd):
    try:
        print("Client Address: ",clientAdd)
        # if(count%2==0):
        #     listBox.insert("", "end", values=clientAdd+('Kết nối',),tags=("chan",))
        # else:
        #     listBox.insert("", "end", values=clientAdd+('Kết nối',),tags=("le",))
        # count+=1

        chat(server,clientAdd)

        print("Client :",clientAdd , "end.")
        soc.close()
        # if(count%2==0):
        #     listBox.insert("", "end", values=clientAdd+('Ngắt kết nối',),tags=("chan",))
        # else:
        #     listBox.insert("", "end", values=clientAdd+('Ngắt kết nối',),tags=("le",))
        # count+=1
    except:
        # thr.join()
        print('Errot at handle')




OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


root = Tk()
root.title('Giá Vàng')
root.geometry("1199x910")
#root.configure(bg = "#A9C1C0")

def raise_frame(frame):
    frame.tkraise()

window0 = Frame(root)
window0.grid(row=0, column=0, sticky='news')
raise_frame(window0)

style = ttk.Style()
style.theme_use("default")
style.configure(
    "Treeview",
    background="#cbdad9",
    foreground = "green",
    rowheight=35,
    fieldbackground="#DEFFF9"
    )


style.map("Treeview",background=[('selected','#FFB2B2')])

cols = ('IP','Port','Hoạt động')
listBox = ttk.Treeview(root, columns=cols, show='headings')
# set column headings


listBox.tag_configure('chan',background="#C7E4FF")
listBox.tag_configure('le',background="#ffffff")

for col in cols:
    listBox.heading(col, text=col)    
listBox.place(x=28, y=300,width=1150,height=595)

# global endThread
# endThread = False

def runServer():
    nClient = 0
    while(nClient<10):       
        try:
            global server, clientAdd
            server, clientAdd =soc.accept()
        
            global thr
            thr = threading.Thread(target=handleClient, args=(server,clientAdd))
            thr.daemon = False
            thr.start()
            global endThread 
            if endThread:
                break
        except Exception as s: #Bắt trường hợp client đóng kết nối đột ngột
            print(s)
            soc.close()
            break
            print("Error")
        nClient+=1

    print("End server")


thr2= threading.Thread(target=lambda: runServer())
thr2.start()



bg0=PhotoImage(file=relative_to_assets("serverMenu.png"))
label_0=Label(window0,image=bg0)
label_0.pack(expand=True,fill=BOTH)

textBox = Label(window0,text=hostAdd, font="Times 22", background="#cbdad9",)
textBox.place(x=60,y=175)


textBox = Label(window0,text=hostPort, font="Times 22", background="#cbdad9",)
textBox.place(x=495,y=175)


def button1Fun():
    button_1.configure(state="disable")
    for i in listBox.get_children():
        listBox.delete(i)
    window0.update()
    endThread=True
    thr2.join()
    server.shutdown(socket.SHUT_RDWR)
    soc.close()
    print("close all")


button_image_1 = PhotoImage(file=relative_to_assets("Button.png"))
button_1 = Button(image=button_image_1,cursor="hand2", bg="#a9c1c0", activebackground="#a9c1c0",borderwidth=0,highlightthickness=0,command=lambda: button1Fun(),relief="flat")
button_1.place(x=925,y=155,width=237.0,height=85.0)


root.resizable(False, False)
root.mainloop()
soc.close()
