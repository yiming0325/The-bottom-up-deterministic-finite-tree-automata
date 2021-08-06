import Tkinter as tk
import pickle
from treeautomaton import *
import tkMessageBox
import easygui
from basedesk import basedesk
from normal_face import normal_face
from max_face import max_face



root = tk.Tk()
base = basedesk(root)


def do_job():
    pass

def info():
    tmp = ""
    for line in lines(open('info.txt','r')):
       tmp = tmp+line 
    easygui.msgbox(tmp)

def max_change():
    base.max_change()

def normal_change():
    base.normal_change()

menubar = tk.Menu(root)

filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Clearall', command = base.clear_all)
filemenu.add_separator()
filemenu.add_command(label='Exit', command = root.quit)

windowmenu = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label='Window', menu = windowmenu)
windowmenu.add_command(label='max', command = max_change)
windowmenu.add_command(label='normal', command = normal_change)

helpmenu = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label='Help', menu = helpmenu)
helpmenu.add_command(label='Info', command = info)

root.config(menu=menubar)

root.mainloop()
