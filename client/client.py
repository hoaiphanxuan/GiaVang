import socket
import pandas as pd

FORMAT = "UTF8"

##lib of gui
import ctypes 
from pathlib import Path

from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk
import os, sys

import time
from tkcalendar import Calendar
from datetime import date, datetime




def sendList(client, list):

    for item in list:
        client.sendall(item.encode(FORMAT))
        #wait response
        client.recv(1024)
        print(item)

    msg = "end"
    client.send(msg.encode(FORMAT))

def recvList(client):
    list = []

    item = client.recv(1024).decode(FORMAT)

    while (item != "end"):
        if(item=="null"):
            item="  "
            
        list.append(item)
        print(list)
        #response
        client.sendall(item.encode(FORMAT))
        item = client.recv(1024).decode(FORMAT)
        print('check2')
    client.send('end'.encode())
    return list
def login(username,password):
    try:
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
    except:
        return '-1'
def signUp(username,password):
    try:
        client.sendall('sign up'.encode())
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
    except:
        return '-1'

def chat(client, typee, area, day):
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
        try:
            listt=[typee,area,day]
            print(listt)
            sendList(client,listt)
            msg=client.recv(1024).decode() 
            dic=[]
            dt=[]
            for i in range (int(msg)):
                l=recvList(client)
                print(l)
                dt.append(l)
                data = {'Lo???i v??ng':l[0],'Gi?? mua v??o':l[2],'Gi?? b??n ra': l[1],'C??ng ty': l[3],'Khu v???c': l[4],'Ng??y c???p nh???t':l[5]}
                dic.append(data)
            df=pd.DataFrame(data=dic)   
            print(df)
            return dt
        except:
            return ['NULL']
# try:
#     client.connect((serverAdd, serverPort))
#     #client.send('sign up'.encode(FORMAT))
#     #msg=client.recv(1024).decode()
#     #signUp(client)
#     # chat(client)
    

# except:  # B???t tr?????ng h???p server b??? ????ng
#     print("Error")
# #.......







OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def raise_frame(frame):
    frame.tkraise()

root = Tk()
root.title('Gi?? V??ng')
root.geometry("1199x910")
#root.configure(bg = "#A9C1C0")

window1 = Frame(root)
window2 = Frame(root)
window3 = Frame(root)
window4 = Frame(root)

for frame in (window1, window2, window3, window4):
    frame.grid(row=0, column=0, sticky='news')



########GUI man hinh hien thi ket qua
bg4=PhotoImage(file=relative_to_assets('TraCuu.png'))
label_4=Label(window4,image=bg4)
label_4.pack()



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

cols = ('Lo???i V??ng',  'Gi?? mua v??o', 'Gi?? b??n ra','C??ng ty', 'Nh??n Hi???u', 'Ng??y C???p Nh???t')
listBox = ttk.Treeview(window4, columns=cols, show='headings')
# set column headings

for col in cols:
    listBox.heading(col, text=col)    
listBox.place(x=21, y=282,width=1156,height=615)


listBox.tag_configure('chan',background="#C7E4FF")
listBox.tag_configure('le',background="#ffffff")


def showInfo():
    typee = ComboLV.get()
    area = ComboKV.get()
    day = cal.selection_get()
    date_object = datetime.strftime(day, "%Y-%m-%d")
   
    year=date_object[0:4]
    month=date_object[5:7]
    dayy=date_object[-2:]
    date_object=year+month+dayy

    print(type(date_object), " ", date_object)

    current_time = datetime.now()
    a = current_time.year*10000+current_time.month*100+current_time.day
    if(a < int(date_object)):
        ctypes.windll.user32.MessageBoxW(0, "V?????t qua ng??y hi???n t???i!", "Th??ng b??o", 0)
    else:
        data=chat(client, typee , area, date_object)

        for i in listBox.get_children():
            listBox.delete(i)
        window4.update()

        if(data==['NULL']):
            ctypes.windll.user32.MessageBoxW(0, "Server ???? ng???t k???t n???i!", "Th??ng b??o", 0)
            raise_frame(window1)
        else: 
            count=0
            for i, (tp, buy, sell, company, area, dayy) in enumerate(data, start=1):
                if(count%2==0):
                    listBox.insert("", "end", values=(tp, buy, sell, company, area, dayy),tags=("chan",))
                else:
                    listBox.insert("", "end", values=(tp, buy, sell, company, area, dayy),tags=("le",))
                count+=1


global today
today= str (date.today())
year=int(today[0:4])
month=int(today[5:7])
day=int(today[-2:])
cal = Calendar(window4,
               font="Times 14", selectmode='day',
               cursor="hand2", year=year, month=month, day=day)

button_GetDate = Button(window4,text="Ch???n", font="Times 16", bg="#66a6ff", cursor="hand2", borderwidth=4, highlightthickness=4,
    command= lambda: {button_14.config(text=cal.selection_get()),cal.place_forget(),button_GetDate.place_forget()},
    relief="flat",
)
button_14 = Button( window4, text=today, font="Times 24", cursor="hand2", bg="white", activebackground="white", borderwidth=0, highlightthickness=0,
    command= lambda:{ cal.place(x=40,y=210,width=400,height=400),button_GetDate.place(x=190,y=620)},#window5.tkraise(),
    relief="flat"
)
button_14.place( x=38.0, y=153.9999999999999, width=286.0, height=58.0)

OPTIONS = [
"T???t c???",
"SJC",
# "V??ng SJC 1L",
# "V??ng nh???n SJC 99,99 0,5 ch???",
# "V??ng nh???n SJC 99,99 1 ch???, 2 ch???, 5 ch???",
# "V??ng n??? trang 99,99%",
# "V??ng n??? trang 99%",
# "V??ng n??? trang 75%",
# "V??ng n??? trang 58,3%",
# "V??ng n??? trang 41,7%",
"AVPL / DOJI CT bu??n",
"AVPL / DOJI CT l???",
"AVPL / DOJI HCM bu??n",
"AVPL / DOJI HCM l???",
"AVPL / DOJI ??N bu??n",
"AVPL / DOJI ??N l???",
"AVPL / DOJI HN bu??n",
"AVPL / DOJI HN l???",
"Nguy??n li??u 9999 - HN",
"Nguy??n li??u 999 - HN",
"Kim Ng??u",
"Kim Th???n T??i",
"L???c Ph??t T??i",
"H??ng Th???nh V?????ng",
"Nh???n H.T.V",
"Nguy??n li???u 99.99",
"Nguy??n li???u 9999",
"Nguy??n li???u 99.9",
"Nguy??n li???u 999",
"Nguy??n li???u 999",
"N??? trang 99.99",
"N??? trang 99.9",
"N??? trang 99",
"N??? trang 18k",
"N??? trang 16k",
"N??? trang 68",
"N??? trang 14k",
"N??? trang 68",
"N??? trang 10k",
] 

ComboLV = ttk.Combobox(window4, value=OPTIONS, width=20, font="Times 14")
ComboLV.place(x=388, y=153, width=260.0, height=58.0)
ComboLV.current(0)



OPTIONS = [
"T???t c???",
#"Long Xuy??n",
#"B???c Li??u",
#"Bi??n H??a",
#"C?? Mau",
"H?? N???i",
"H??? Ch?? Minh",
#"Mi???n T??y",
#"Nha Trang",
#"Qu??ng Ng??i",
# "????  N???ng",
# "B??nh Ph?????c",
# "H??? Long",
# "Phan Rang",
# "Qu???ng Nam",
# "Quy Nh??n",
# "Hu???",
"Nh???n DOJI H??ng Th???nh V?????ng",
"MARITIME BANK",
"SACOMBANK",
"Mi H???ng SJC",
"Ng???c H???i SJC HCM",
"Ng???c H???i SJC Long An",
"Ng???c H???i SJC T??n Hi???p",
"PH?? QU?? SJC",
"SPOT GOLD",
"OIL",
"Nh???n PH?? QU?? 24K",
"Mi H???ng 999",
"Nh???n SJC 99,99",
"Ng???c H???i 24K HCM",
"Ng???c H???i 24K Long An",
"Ng???c H???i 24K T??n Hi???p",
"Mi H???ng 985",
"Mi H???ng 980",
"Ng???c H???i 17K HCM",
"Ng???c H???i 17K Long An",
"Ng???c H???i 17K T??n Hi???p",
"Mi H???ng 750",
"Mi H???ng 680",
"Mi H???ng 610",
"Mi H???ng 950",
] 
def selected(event):
    print("brand: " + ComboKV.get())


ComboKV = ttk.Combobox(window4, value=OPTIONS, width=20, font="Times 14")
ComboKV.place(x=708.0, y=153, width=260.0, height=58.0)
ComboKV.current(0)



button_image_44 = PhotoImage(file=relative_to_assets("button_4.png"))
button_44 = Button( window4, cursor="hand2", image=button_image_44, bg="#a9c1c0", activebackground="#a9c1c0", borderwidth=0, highlightthickness=0,
    command=lambda: {ComboKV.current(0),ComboLV.current(0),button_14.config(text=today)},
    relief="flat"
)
button_44.place(x=1015.0, y=144.9999999999999, width=60.021484375, height=66.0)



button_image_54 = PhotoImage(file=relative_to_assets("button_5.png"))
button_54 = Button( window4, cursor="hand2", image=button_image_54,  bg="#a9c1c0", activebackground="#a9c1c0", borderwidth=0, highlightthickness=0,
    command=lambda: showInfo(),
    relief="flat"
)


flag1 = 0

def funButtonDiscon():
    #client.send('xxx'.encode())
    client.close()
    raise_frame(window1)
    global flag1
    flag1 = 1

button_54.place(x=1116.0, y=144.9999999999999, width=60.0, height=66.0)

button_image_64 = PhotoImage( file=relative_to_assets("button_6.png"))
button_64 = Button(window4, cursor="hand2",image=button_image_64, bg="#a9c1c0",activebackground="#a9c1c0", borderwidth=0, highlightthickness=0,
    command=lambda: funButtonDiscon(),
    relief="flat"
)
button_64.place( x=959, y=21, width=217.0, height=66.0)




#GUI ????NG K??

bg3=PhotoImage(file=relative_to_assets('DangKi.png'))
label_3=Label(window3,image=bg3)
label_3.pack(expand=True,fill=BOTH)


entry_13 = Entry(window3, bd=0, bg='#d7e2e2', highlightthickness=0, font = "Times 22")
entry_13.place(  x=614.018798828125, y=330, width=550, height=58)


### NH???P MK
#an mat khau
def toggle_password3():
    if entry_23.cget('show') == '':
        entry_23.config(show='*')
    else:
        entry_23.config(show='')

entry_23 = Entry(window3,show='*',bd=0, bg='#d7e2e2', highlightthickness=0, font = "Times 22")
entry_23.place( x=614.018798828125, y=481, width=550, height=55)

##### BUTTON ???N MK
buton_hide_image3=PhotoImage(file=relative_to_assets("hide.png"))
buton_hide3 = Button(window3,cursor='hand2',image=buton_hide_image3, bg='#d7e2e2', activebackground='#d7e2e2', borderwidth=0, highlightthickness=0,
    command= lambda: toggle_password3(),
    relief='flat'
    )
buton_hide3.place( x=1120, y=480, width=40, height=58,)

def callSignUp():
    flag = signUp(entry_13.get(),entry_23.get())
    if(flag=='-1'):
        ctypes.windll.user32.MessageBoxW(0, "Server ???? ng???t k???t n???i!", "Th??ng b??o", 0)
        raise_frame(window1)
    if(flag=='0'):
        ctypes.windll.user32.MessageBoxW(0, "T??i kho???n v?? m???t kh???u kh??ng ???????c ????? tr???ng!", "Th??ng b??o", 0)
    if(flag=='1'):
        ctypes.windll.user32.MessageBoxW(0, "????ng k?? t??i kho???n th??nh c??ng!", "Th??ng b??o", 0)
        raise_frame(window2)
    if(flag=='2'):
        ctypes.windll.user32.MessageBoxW(0, "T??i kho???n ???? t???n t???i!", "Th??ng b??o", 0)


#button gui tai khoan dang ky
button_image_13 = PhotoImage( file=relative_to_assets("button_1_dk.png"))
button_13 = Button( window3,cursor='hand2', image=button_image_13,bg='#d7e2e2',activebackground='#d7e2e2', borderwidth=0,highlightthickness=0, command=lambda: callSignUp(), relief="flat")
button_13.place( x=772.0, y=561.0, width=265.0,height=78.0)
#button chuyen sang trang dang nhap
button_image_23 = PhotoImage( file=relative_to_assets("button_2_dk.png"))
button_23 = Button( window3,cursor='hand2', image=button_image_23,bg='#d7e2e2',activebackground='#d7e2e2', borderwidth=0,highlightthickness=0, command=lambda: raise_frame(window2), relief="flat")
button_23.place( x=732.0, y=659.0, width=354.5205078125, height=36.5087890625)




####GUI ????NG NH???P

bg2 = PhotoImage(file=relative_to_assets( "DangNhap.png"))
# Show image using label
label2 = Label( window2, image = bg2)
label2.pack()

entry_12 = Entry(window2, bd=0, bg='#d7e2e2', highlightthickness=0, font = "Times 22")
entry_12.place(  x=614.018798828125, y=330, width=550, height=58)

### NH???P MK
#an mat khau
def toggle_password():
    if entry_22.cget('show') == '':
        entry_22.config(show='*')
    else:
        entry_22.config(show='')

entry_22 = Entry( window2,show='*', bd=0,  bg='#d7e2e2',highlightthickness=0, font = "Times 22")
entry_22.place( x=614.018798828125,  y=480, width=550, height=56)

##### BUTTON ???N MK
buton_hide_image2=PhotoImage( file=relative_to_assets("hide.png"))
buton_hide2 = Button(window2,cursor='hand2',image=buton_hide_image2, bg='#d7e2e2',activebackground='#d7e2e2',borderwidth=0, highlightthickness=0,
    command= lambda: toggle_password(),
   relief='flat'
)
buton_hide2.place( x=1120, y=480, width=40,height=55)


######### BUTTON ????NG NH???P
def callLogin():
    flag = login(entry_12.get(),entry_22.get())
    if(flag=='-1'):
        ctypes.windll.user32.MessageBoxW(0, "Server ???? ng???t k???t n???i!", "Th??ng b??o", 0)  
        raise_frame(window1)  
    if(flag=='0'):
        ctypes.windll.user32.MessageBoxW(0, "T??i kho???n v?? m???t kh???u kh??ng ???????c ????? tr???ng", "Th??ng b??o", 0)
    if(flag=='1'):
        raise_frame(window4)
        for i in listBox.get_children():
            listBox.delete(i)
        window4.update()
    if(flag=='2'):
        ctypes.windll.user32.MessageBoxW(0, "M???t kh???u kh??ng ????ng", "Th??ng b??o", 0)
    if(flag=='3'):
        ctypes.windll.user32.MessageBoxW(0, "Kh??ng t??m th???y t??i kho???n", "Th??ng b??o", 0)
button_image_12 = PhotoImage( file=relative_to_assets("button_1.png"))
button_12 = Button( window2,cursor='hand2', image=button_image_12, bg='#d7e2e2', activebackground='#d7e2e2', borderwidth=0, highlightthickness=0, command=lambda: callLogin(), relief="flat")
button_12.place( x=771.0, y=560.0, width=265.0, height=78.0)


####### BUTTON ????NG K??
button_image_22 = PhotoImage(file=relative_to_assets("button_2.png"))
button_22 = Button(window2,cursor='hand2',image=button_image_22,bg='#d7e2e2',activebackground='#d7e2e2',borderwidth=0,highlightthickness=0,command= lambda: {raise_frame(window3)},relief="flat")
button_22.place(x=749.0,  y=656.0, width=350.3861083984375, height=36.60003662109375)



############### GUI WELCOME
bg1=PhotoImage(file=relative_to_assets('Welcom.png'))
label_1=Label(window1,image=bg1)
label_1.pack()

serverAdd = StringVar()
serverAdd.set("192.168.1.6")

serverPort=StringVar()
serverPort.set("63215")

entry_ip_welcom = Entry(window1,textvariable = serverAdd,font="Times 22", bd=0, bg='#d7e2e2', highlightthickness=0)
entry_ip_welcom.place(x=609.00634765625, y=333.2843017578125, width=550.5, height=56.89031982421875)

entry_port_welcom = Entry(window1,textvariable=serverPort,font="Times 22",bd=0,bg='#d7e2e2',highlightthickness=0)
entry_port_welcom.place(x=609.00634765625,y=483.361328125,width=550.5,height=56.8902587890625)

def ketnoi():
    serverAdd = (entry_ip_welcom.get())
    serverPort = (int(entry_port_welcom.get()))
    try:
        global client
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        client.connect((serverAdd, serverPort))
        raise_frame(window2)
    except:  # B???t tr?????ng h???p server b??? ????ng
        if flag1==0:
            ctypes.windll.user32.MessageBoxW(0, "Kh??ng th??? k???t n???i v???i Server!", "Th??ng b??o", 0)
        else:
            ctypes.windll.user32.MessageBoxW(0, "B???n c???n ch???y l???i ch????ng tr??nh!", "Th??ng b??o", 0)
    


button_welcom = PhotoImage(
    file=relative_to_assets("bt_welcom.png"))
button_1_wc = Button(window1, image=button_welcom,borderwidth=0,bg="#d7e2e2", activebackground="#d7e2e2",highlightthickness=0,
    command=lambda: ketnoi(), relief="flat")
button_1_wc.place(x=763.0,y=561.0,width=239.0,height=77.0)



root.resizable(False, False)
raise_frame(window1)
root.mainloop()
#client.send('xxx'.encode())
client.close()

