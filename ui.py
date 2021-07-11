import Tkinter as tk
import pickle
from treeautomaton import *
import tkMessageBox
import easygui
from normal_face import normal_face
from max_face import max_face


class basedesk():
    def __init__(self,master):
        self.root = master
        self.root.resizable(0,0)
        self.root.title('Welcome to Tree Automata')

        # welcome image
        self.canvas = tk.Canvas(self.root, height=200, width=450)
        self.image_file = tk.PhotoImage(file='welcome.gif')
        self.image = self.canvas.create_image(0, 0, anchor='nw', image=self.image_file)
        self.create_base()

        self.face= normal_face(self.root)

    def create_base(self):
        self.canvas.pack(side='top')

    
    def normal_change(self):
        self.face.destroy()
        self.face = normal_face(self.root)

    def max_change(self):
        self.face.destroy()
        self.face = max_face(self.root)

    def clear_all(self):
        self.face.clear_all()

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
filemenu.add_command(label='Save', command = do_job)
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
