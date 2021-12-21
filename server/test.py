from datetime import date
import json
import threading
import time
from threading import Thread
import ctypes  # An included library with Python install.   
from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
from datetime import date
### ẩn hiện pass

# def toggle_password():
#     if passwd_entry.cget('show') == '':
#         passwd_entry.config(show='*')
#         toggle_btn.config(text='Show Password')
#     else:
#         passwd_entry.config(show='')
#         toggle_btn.config(text='Hide Password')

# root = tk.Tk()

# passwd_entry = tk.Entry(root, show='*', width=20)
# passwd_entry.pack(side=tk.LEFT)

# toggle_btn = tk.Button(root, text='Show Password', width=15, command=toggle_password)
# toggle_btn.pack(side=tk.LEFT)

# root.mainloop()



########################


#####list xổ xuống

# from tkcalendar import Calendar, DateEntry
# master = Tk()
# master.geometry("1000x1000")
# #master.configure(bg = "#A9C1C0")
# f1=Frame(master)
# f2=Frame(master)

# f1.grid(row=0, column=0, sticky='news')
# f2.grid(row=0, column=0, sticky='news')


# variable = StringVar(master)
# variable.set("xxx") # default value

# bg=PhotoImage(file='1.png')
# bg_1=Label(f1,image=bg)
# bg_1.pack()

# today= str (date.today())
# year=int(today[0:4])
# month=int(today[5:7])
# day=int(today[-2:])
# cal = Calendar(f1,
#                font="Times 14", selectmode='day',
#                cursor="hand2", year=year, month=month, day=day)
# cal.place(x=100,y=100,width=500,height=500)


# b1=Button(f2,text='back',command= lambda: print(cal.selection_get()),bg='#d7e2e2', activebackground='#d7e2e2', borderwidth=0, highlightthickness=0,)
# b1.place(x=100,y=100,width=10,height=10)
# Button(f1,text='next',command= lambda: f2.tkraise()).place(x=0,y=0,width=10,height=10)



# f1.tkraise()

# mainloop()

cal.pack(fill="both", expand=True)
w = OptionMenu(master, variable, "d","x")
print (variable.get())

cal.pack()


# def updateData(a):
#     while (a):
#         time.sleep(4)
#         print('do something')
        


# try:
#     print('a')
#     t=time.perf_counter()
#     threadUpdate=threading.Thread(target=updateData,args=(1,))
#     threadUpdate.startaaa()
#     for i in range(1,5):
#         print(time.perf_counter()-t)
#     print('load')
#     threadUpdate.end()
# except:
#     print('error')










# try:
#     import tkinter as tk                # python 3
#     from tkinter import font as tkfont  # python 3
# except ImportError:
#     import Tkinter as tk     # python 2
#     import tkFont as tkfont  # python 2

# class SampleApp(tk.Tk):

#     def __init__(self, *args, **kwargs):
#         tk.Tk.__init__(self, *args, **kwargs)

#         self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

#         # the container is where we'll stack a bunch of frames
#         # on top of each other, then the one we want visible
#         # will be raised above the others
#         container = tk.Frame(self)
#         container.pack(side="top", fill="both", expand=True)
#         container.grid_rowconfigure(0, weight=1)
#         container.grid_columnconfigure(0, weight=1)

#         self.frames = {}
#         for F in (StartPage, PageOne, PageTwo):
#             page_name = F.__name__
#             frame = F(parent=container, controller=self)
#             self.frames[page_name] = frame

#             # put all of the pages in the same location;
#             # the one on the top of the stacking order
#             # will be the one that is visible.
#             frame.grid(row=0, column=0, sticky="nsew")

#         self.show_frame("StartPage")

#     def show_frame(self, page_name):
#         '''Show a frame for the given page name'''
#         frame = self.frames[page_name]
#         frame.tkraise()


# class StartPage(tk.Frame):

#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         label = tk.Label(self, text="This is the start page", font=controller.title_font)
#         label.pack(side="top", fill="x", pady=10)

#         button1 = tk.Button(self, text="Go to Page One",
#                             command=lambda: controller.show_frame("PageOne"))
#         button2 = tk.Button(self, text="Go to Page Two",
#                             command=lambda: controller.show_frame("PageTwo"))
#         button1.pack()
#         button2.pack()


# class PageOne(tk.Frame):

#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         label = tk.Label(self, text="This is page 1", font=controller.title_font)
#         label.pack(side="top", fill="x", pady=10)
#         button = tk.Button(self, text="Go to the start page",
#                            command=lambda: controller.show_frame("StartPage"))
#         button.pack()


# class PageTwo(tk.Frame):

#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         label = tk.Label(self, text="This is page 2", font=controller.title_font)
#         label.pack(side="top", fill="x", pady=10)
#         button = tk.Button(self, text="Go to the start page",
#                            command=lambda: controller.show_frame("StartPage"))
#         button.pack()


# if __name__ == "__main__":
#     app = SampleApp()
#     app.mainloop()



try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk

from tkcalendar import Calendar, DateEntry

def example1():
    def print_sel():
        print(cal.selection_get())

    top = tk.Toplevel(root)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1", year=2018, month=2, day=5)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()

def example2():
    top = tk.Toplevel(root)

    ttk.Label(top, text='Choose date').pack(padx=10, pady=10)

    cal = DateEntry(top, width=12, background='darkblue',
                    foreground='white', borderwidth=2)
    cal.pack(padx=10, pady=10)

root = tk.Tk()
s = ttk.Style(root)
s.theme_use('clam')

ttk.Button(root, text='Calendar', command=example1).pack(padx=10, pady=10)
ttk.Button(root, text='DateEntry', command=example2).pack(padx=10, pady=10)

root.mainloop()




# chông các màn hình

# from tkinter import *


# def raise_frame(frame):
#     frame.tkraise()

# root = Tk()

# f1 = Frame(root)
# f2 = Frame(root)
# f3 = Frame(root)
# f4 = Frame(root)

# for frame in (f1, f2, f3, f4):
#     frame.grid(row=0, column=0, sticky='news')

# Button(f1, text='Go to frame 2', command=lambda:raise_frame(f2)).pack()
# Label(f1, text='FRAME 1').pack()

# Label(f2, text='FRAME 2').pack()
# Button(f2, text='Go to frame 3', command=lambda:raise_frame(f3)).pack()

# Label(f3, text='FRAME 3').pack(side='left')
# Button(f3, text='Go to frame 4', command=lambda:raise_frame(f4)).pack(side='left')

# Label(f4, text='FRAME 4').pack()
# Button(f4, text='Goto to frame 1', command=lambda:raise_frame(f1)).pack()

# raise_frame(f1)
# root.mainloop()