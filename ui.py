import Tkinter as tk
from treeautomaton import *
import easygui

window = tk.Tk()
window.title('Welcome to Tree Automata')
window.geometry('650x700')

# welcome image
canvas = tk.Canvas(window, height=200, width=450)
image_file = tk.PhotoImage(file='welcome.gif')
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
canvas.pack(side='top')

# "---------1. Create Automata-----------------"
tk.Label(window, text='1. Create automaton', font=('Arial', 12)).place(x=30, y=150)

tk.Label(window, text='F:', font=('Arial', 12)).place(x=60, y=190)
frm_5 = tk.Frame(window)
frm_5.place(x=90, y=190)
scrollbar_5 = tk.Scrollbar(frm_5)
Text_1 = tk.Text(frm_5, height=3, width=30, yscrollcommand=scrollbar_5.set)
scrollbar_5.config(command=Text_1.yview)
scrollbar_5.pack(side='right', fill='y')
Text_1.pack(side="left")
def confirm_1():
    tmp_string = Text_1.get("1.0", "end")
    print (tmp_string)
Button_1 = tk.Button(window, text='confirm', command=confirm_1)
Button_1.place(x=360, y=190)
def clear_12():
    Text_1.delete('1.0','end')
Button_12 = tk.Button(window, text='clear', command=clear_12)
Button_12.place(x=420, y=190)

tk.Label(window, text='Q:', font=('Arial', 12)).place(x=60, y=250)
frm_4 = tk.Frame(window)
frm_4.place(x=90, y=250)
scrollbar_4 = tk.Scrollbar(frm_4)
Text_2 = tk.Text(frm_4, height=3, width=30, yscrollcommand=scrollbar_4.set)
scrollbar_4.config(command=Text_2.yview)
scrollbar_4.pack(side='right', fill='y')
Text_2.pack(side="left")
def confirm_2():
    tmp_string = Text_2.get("1.0", "end")
    print (tmp_string)
Button_2 = tk.Button(window, text='confirm', command=confirm_2)
Button_2.place(x=360, y=250)
def clear_11():
    Text_2.delete('1.0','end')
Button_11 = tk.Button(window, text='clear', command=clear_11)
Button_11.place(x=420, y=250)

tk.Label(window, text='Qf:', font=('Arial', 12)).place(x=60, y=310)
frm_3 = tk.Frame(window)
frm_3.place(x=90, y=310)
scrollbar_3 = tk.Scrollbar(frm_3)
Text_3 = tk.Text(frm_3, height=3, width=30, yscrollcommand=scrollbar_3.set)
scrollbar_3.config(command=Text_3.yview)
scrollbar_3.pack(side='right', fill='y')
Text_3.pack(side="left")
def confirm_3():
    tmp_string = Text_3.get("1.0", "end")
    file = open('finalsymbols_1.txt','w')
    file.write(tmp_string)
    file.close()
Button_3 = tk.Button(window, text='confirm', command=confirm_3)
Button_3.place(x=360, y=310)
def clear_10():
    Text_3.delete('1.0','end')
Button_10 = tk.Button(window, text='clear', command=clear_10)
Button_10.place(x=420, y=310)

tk.Label(window, text=unichr(0x394)+':', font=('Arial', 12)).place(x=60, y=370)
frm_2 = tk.Frame(window)
frm_2.place(x=90, y=370)
scrollbar_2 = tk.Scrollbar(frm_2)
Text_4 = tk.Text(frm_2, height=3, width=30, yscrollcommand=scrollbar_2.set)
scrollbar_2.config(command=Text_4.yview)
scrollbar_2.pack(side='right', fill='y')
Text_4.pack(side="left")
def confirm_4():
    tmp_string = Text_4.get("1.0", "end")
    file = open('productions_1.txt','w')
    file.write(tmp_string)
    file.close()
Button_4 = tk.Button(window, text='confirm', command=confirm_4)
Button_4.place(x=360, y=370)
def clear_9():
    Text_4.delete('1.0','end')
Button_9 = tk.Button(window, text='clear', command=clear_9)
Button_9.place(x=420, y=370)
# "--------------------------"


# "---------2. Simulate Automata-----------------"
tk.Label(window, text='2. Simulate automaton', font=('Arial', 12)).place(x=30, y=430)
tk.Label(window, text='Input the tree:', font=('Arial', 12)).place(x=60, y=455)


Text_5 = tk.Text(window, height=1, width=30)
Text_5.place(x=90, y=485)


def confirm_5():
    tmp_string = Text_5.get("1.0", "end")
    file = open('input_string.txt','w')
    file.write(tmp_string)
    file.close()
Button_5 = tk.Button(window, text='confirm', command=confirm_5)
Button_5.place(x=350, y=480)

def clear_8():
    Text_5.delete('1.0','end')

Button_8 = tk.Button(window, text='clear', command=clear_8)
Button_8.place(x=410, y=480)
# "--------------------------"

# "---------3. Transition graph-----------------"
tk.Label(window, text='3. Transition graph', font=('Arial', 12)).place(x=30, y=510)

frm_1 = tk.Frame(window)
frm_1.place(x=90, y=540)

scrollbar_1 = tk.Scrollbar(frm_1)
Text_6 = tk.Text(frm_1, height=8, width=50, yscrollcommand=scrollbar_1.set)
scrollbar_1.config(command=Text_6.yview)
scrollbar_1.pack(side='right', fill='y')
Text_6.pack(side="left")

def lines(file_stream):
    for line in file_stream:
        yield line

def display():
    run()
    for line in lines(open('display.txt','r')):
        Text_6.insert('end', line)

Button_6 = tk.Button(window, text='display', command=display)
Button_6.place(x=515, y=540)

def clear_7():
    Text_6.delete('1.0','end')

Button_7 = tk.Button(window, text='clear', command=clear_7)
Button_7.place(x=515, y=580)
# "--------------------------"

# "---------Menu-----------------"
def do_job():
    pass

def info():
    tmp = ""
    for line in lines(open('info.txt','r')):
       tmp = tmp+line 
    easygui.msgbox(tmp)

def clear_all():
    clear_7()
    clear_8()
    clear_9()
    clear_10()
    clear_11()
    clear_12()

menubar = tk.Menu(window)

filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Save', command = do_job)
filemenu.add_command(label='Clearall', command = clear_all)
filemenu.add_separator()
filemenu.add_command(label='Exit', command = window.quit)

helpmenu = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label='Help', menu = helpmenu)
helpmenu.add_command(label='Info', command = info)

window.config(menu=menubar)

# "--------------------------"
window.mainloop()


