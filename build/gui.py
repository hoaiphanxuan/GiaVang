
import ctypes 
from pathlib import Path

from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk
import os, sys
lib_path = os.path.abspath(os.path.join('../client'))
# thêm thư mục cần load vào trong hệ thống
sys.path.append(lib_path)
from client import *
import time
from tkcalendar import Calendar
from datetime import date


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


try:
    client.connect((serverAdd, serverPort))
except:  # Bắt trường hợp server bị đóng
    print("Error")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def raise_frame(frame):
    frame.tkraise()

root = Tk()
root.title('Giá Vàng')
root.geometry("1203x915")
#root.configure(bg = "#A9C1C0")

window1 = Frame(root)
window2 = Frame(root)
window3 = Frame(root)
window4 = Frame(root)

for frame in (window1, window2, window3, window4):
    frame.grid(row=0, column=0, sticky='news')


########GUI man hinh hien thi ket qua
bg4=PhotoImage(file='TraCuu.png')
label_4=Label(window4,image=bg4)
label_4.pack()

today= str (date.today())
year=int(today[0:4])
month=int(today[5:7])
day=int(today[-2:])
cal = Calendar(window4,
               font="Times 14", selectmode='day',
               cursor="hand2", year=year, month=month, day=day)

button_GetDate = Button(window4,text="Chọn", font="Times 16", bg="#66a6ff", cursor="hand2", borderwidth=4, highlightthickness=4,
    command= lambda: {button_14.config(text=cal.selection_get()),cal.place_forget(),button_GetDate.place_forget()},
    relief="flat",
)
button_14 = Button( window4, text=today, font="Times 24", cursor="hand2", bg="#cbdad9", activebackground="#cbdad9", borderwidth=0, highlightthickness=0,
    command= lambda:{ cal.place(x=40,y=210,width=400,height=400),button_GetDate.place(x=190,y=620)},#window5.tkraise(),
    relief="flat"
)
button_14.place( x=40.0, y=151.9999999999999, width=286.0, height=58.0)

def LoaiVang():
    OPTIONS = [
    "Vàng SJC",
    "Vàng SJC 1L",
    "Vàng nhẫn SJC 99,99 0,5 chỉ",
    "Vàng nhẫn SJC 99,99 1 chỉ, 2 chỉ, 5 chỉ",
    "Vàng nữ trang 99,99%",
    "Vàng nữ trang 99%",
    "Vàng nữ trang 75%",
    "Vàng nữ trang 58,3%",
    "Vàng nữ trang 41,7%",
    "AVPL / DOJI CT buôn",
    "AVPL / DOJI CT lẻ",
    "AVPL / DOJI HCM buôn",
    "AVPL / DOJI HCM lẻ",
    "AVPL / DOJI ĐN buôn",
    "AVPL / DOJI ĐN lẻ",
    "AVPL / DOJI HN buôn",
    "AVPL / DOJI HN lẻ",
    "Nguyên liêu 9999 - HN",
    "Nguyên liêu 999 - HN",
    "Kim Ngưu",
    "Kim Thần Tài",
    "Lộc Phát Tài",
    "Hưng Thịnh Vượng",
    "Nhẫn H.T.V",
    "Nguyên liệu 99.99",
    "Nguyên liệu 9999",
    "Nguyên liệu 99.9",
    "Nguyên liệu 999",
    "Nguyên liệu 999",
    "Nữ trang 99.99",
    "Nữ trang 99.9",
    "Nữ trang 99",
    "Nữ trang 18k",
    "Nữ trang 16k",
    "Nữ trang 68",
    "Nữ trang 14k",
    "Nữ trang 68",
    "Nữ trang 10k",
    ] 
    def selected(event):
        print("type: " +ComboLV.get())

    ComboLV = ttk.Combobox(window4, value=OPTIONS, width=20, font="Times 14")
    ComboLV.place(x=390, y=151, width=260.0, height=58.0)
    ComboLV.bind("<<ComboboxSelected>>", selected)

button_24 = Button( window4, cursor="hand2", bg="#cbdad9", activebackground="#cbdad9", borderwidth=0, highlightthickness=0,
    command=lambda: LoaiVang(),
    relief="flat"
)
button_24.place(x=390, y=151, width=260.0, height=58.0)

def Khuvuc():
    OPTIONS = [
    "Long Xuyên",
    "Bạc Liêu",
    "Biên Hòa",
    "Cà Mau",
    "Hà Nội",
    "Hồ Chí Minh",
    "Miền Tây",
    "Nha Trang",
    "Quãng Ngãi",
    "Đà  Nẵng",
    "Bình Phước",
    "Hạ Long",
    "Phan Rang",
    "Quảng Nam",
    "Quy Nhơn",
    "Huế",
    "Nhẫn DOJI Hưng Thịnh Vượng",
    "MARITIME BANK",
    "SACOMBANK",
    "Mi Hồng SJC",
    "Ngọc Hải SJC HCM",
    "Ngọc Hải SJC Long An",
    "Ngọc Hải SJC Tân Hiệp",
    "PHÚ QUÝ SJC",
    "SPOT GOLD",
    "OIL",
    "Nhẫn PHÚ QUÝ 24K",
    "Mi Hồng 999",
    "Nhẫn SJC 99,99",
    "Ngọc Hải 24K HCM",
    "Ngọc Hải 24K Long An",
    "Ngọc Hải 24K Tân Hiệp",
    "Mi Hồng 985",
    "Mi Hồng 980",
    "Ngọc Hải 17K HCM",
    "Ngọc Hải 17K Long An",
    "Ngọc Hải 17K Tân Hiệp",
    "Mi Hồng 750",
    "Mi Hồng 680",
    "Mi Hồng 610",
    "Mi Hồng 950",
    ] 
    def selected(event):
        print("brand: " + ComboKV.get())

    ComboKV = ttk.Combobox(window4, value=OPTIONS, width=20, font="Times 14")
    ComboKV.place(x=710.0, y=151, width=260.0, height=58.0)
    ComboKV.bind("<<ComboboxSelected>>", selected)

button_34 = Button(window4, cursor="hand2",bg="#cbdad9",activebackground="#cbdad9",borderwidth=0, highlightthickness=0, 
    command=lambda: Khuvuc(),
    relief="flat"
)
button_34.place( x=710.0, y=151, width=260.0, height=58.0)

button_image_44 = PhotoImage(file=relative_to_assets("button_4.png"))
button_44 = Button( window4, cursor="hand2", image=button_image_44, bg="#a9c1c0", activebackground="#a9c1c0", borderwidth=0, highlightthickness=0,
    command=lambda: print("button_tìm kiếm clicked"), 
    relief="flat"
)
button_44.place(x=1021.0, y=143.9999999999999, width=60.021484375, height=66.0)

button_image_54 = PhotoImage(file=relative_to_assets("button_5.png"))
button_54 = Button( window4, cursor="hand2", image=button_image_54,  bg="#a9c1c0", activebackground="#a9c1c0", borderwidth=0, highlightthickness=0,
    command=lambda: print("button_làm mới clicked"),
    relief="flat"
)
button_54.place(x=1112.0, y=151.9999999999999, width=56.0, height=58.0)

button_image_64 = PhotoImage( file=relative_to_assets("button_6.png"))
button_64 = Button(window4, cursor="hand2",image=button_image_64, bg="#a9c1c0",activebackground="#a9c1c0", borderwidth=0, highlightthickness=0,
    command=lambda: print("button_ngắt kết nối clicked"),
    relief="flat"
)
button_64.place( x=965, y=21, width=255.0, height=66.0)

#GUI ĐĂNG KÝ

bg3=PhotoImage(file='DangKi.png')
label_3=Label(window3,image=bg3)
label_3.pack(expand=True,fill=BOTH)


entry_13 = Entry(window3, bd=0, bg='#d7e2e2', highlightthickness=0, font = "Times 22")
entry_13.place(  x=614.018798828125, y=330, width=550, height=58)


### NHẬP MK
#an mat khau
def toggle_password3():
    if entry_23.cget('show') == '':
        entry_23.config(show='*')
    else:
        entry_23.config(show='')

entry_23 = Entry(window3,show='*',bd=0, bg='#d7e2e2', highlightthickness=0, font = "Times 22")
entry_23.place( x=614.018798828125, y=481, width=550, height=55)

##### BUTTON ẨN MK
buton_hide_image3=PhotoImage(file=relative_to_assets("hide.png"))
buton_hide3 = Button(window3,cursor='hand2',image=buton_hide_image3, bg='#d7e2e2', activebackground='#d7e2e2', borderwidth=0, highlightthickness=0,
    command= lambda: toggle_password3(),
    relief='flat'
    )
buton_hide3.place( x=1120, y=480, width=40, height=58,)

def callSignUp():
    flag = signUp(entry_13.get(),entry_23.get())
    if(flag=='0'):
        ctypes.windll.user32.MessageBoxW(0, "Tài khoản và mật khẩu không được để trống!", "Thông báo", 0)
    if(flag=='1'):
        ctypes.windll.user32.MessageBoxW(0, "Đăng ký tài khoản thành công!", "Thông báo", 0)
        raise_frame(window2)
    if(flag=='2'):
        ctypes.windll.user32.MessageBoxW(0, "Tài khoản đã tồn tại!", "Thông báo", 0)


#button gui tai khoan dang ky
button_image_13 = PhotoImage( file=relative_to_assets("button_1_dk.png"))
button_13 = Button( window3,cursor='hand2', image=button_image_13,bg='#d7e2e2',activebackground='#d7e2e2', borderwidth=0,highlightthickness=0, command=lambda: callSignUp(), relief="flat")
button_13.place( x=772.0, y=561.0, width=265.0,height=78.0)
#button chuyen sang trang dang nhap
button_image_23 = PhotoImage( file=relative_to_assets("button_2_dk.png"))
button_23 = Button( window3,cursor='hand2', image=button_image_23,bg='#d7e2e2',activebackground='#d7e2e2', borderwidth=0,highlightthickness=0, command=lambda: raise_frame(window2), relief="flat")
button_23.place( x=732.0, y=659.0, width=354.5205078125, height=36.5087890625)




####GUI ĐĂNG NHẬP

bg2 = PhotoImage(file = "DangNhap.png")
# Show image using label
label2 = Label( window2, image = bg2)
label2.pack()

entry_12 = Entry(window2, bd=0, bg='#d7e2e2', highlightthickness=0, font = "Times 22")
entry_12.place(  x=614.018798828125, y=330, width=550, height=58)

### NHẬP MK
#an mat khau
def toggle_password():
    if entry_22.cget('show') == '':
        entry_22.config(show='*')
    else:
        entry_22.config(show='')

entry_22 = Entry( window2,show='*', bd=0,  bg='#d7e2e2',highlightthickness=0, font = "Times 22")
entry_22.place( x=614.018798828125,  y=480, width=550, height=56)

##### BUTTON ẨN MK
buton_hide_image2=PhotoImage( file=relative_to_assets("hide.png"))
buton_hide2 = Button(window2,cursor='hand2',image=buton_hide_image2, bg='#d7e2e2',activebackground='#d7e2e2',borderwidth=0, highlightthickness=0,
    command= lambda: toggle_password(),
   relief='flat'
)
buton_hide2.place( x=1120, y=480, width=40,height=55)


######### BUTTON ĐĂNG NHẬP
def callLogin():
    flag = login(entry_12.get(),entry_22.get())
    if(flag=='0'):
        ctypes.windll.user32.MessageBoxW(0, "Tài khoản và mật khẩu không được để trống", "Thông báo", 0)
    if(flag=='1'):
        raise_frame(window4)
    if(flag=='2'):
        ctypes.windll.user32.MessageBoxW(0, "Mật khẩu không đúng", "Thông báo", 0)
    if(flag=='3'):
        ctypes.windll.user32.MessageBoxW(0, "Không tìm thấy tài khoản", "Thông báo", 0)
button_image_12 = PhotoImage( file=relative_to_assets("button_1.png"))
button_12 = Button( window2,cursor='hand2', image=button_image_12, bg='#d7e2e2', activebackground='#d7e2e2', borderwidth=0, highlightthickness=0, command=lambda: callLogin(), relief="flat")
button_12.place( x=771.0, y=560.0, width=265.0, height=78.0)


####### BUTTON ĐĂNG KÝ
button_image_22 = PhotoImage(file=relative_to_assets("button_2.png"))
button_22 = Button(window2,cursor='hand2',image=button_image_22,bg='#d7e2e2',activebackground='#d7e2e2',borderwidth=0,highlightthickness=0,command= lambda: raise_frame(window3),relief="flat")
button_22.place(x=749.0,  y=656.0, width=350.3861083984375, height=36.60003662109375)



root.resizable(False, False)
raise_frame(window4)
root.mainloop()
client.close()


