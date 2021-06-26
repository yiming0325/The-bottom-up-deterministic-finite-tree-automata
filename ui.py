import Tkinter as tk

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
Text_1 = tk.Text(window, height=2, width=30)
Text_1.place(x=90, y=190)
def confirm_1():
    tmp_string = Text_1.get("1.0", "end")
    print (tmp_string)
Button_1 = tk.Button(window, text='confirm', command=confirm_1)
Button_1.place(x=350, y=190)

tk.Label(window, text='Q:', font=('Arial', 12)).place(x=60, y=230)
Text_2 = tk.Text(window, height=2, width=30)
Text_2.place(x=90, y=230)
def confirm_2():
    tmp_string = Text_2.get("1.0", "end")
    print (tmp_string)
Button_2 = tk.Button(window, text='confirm', command=confirm_2)
Button_2.place(x=350, y=230)

tk.Label(window, text='Qf:', font=('Arial', 12)).place(x=60, y=270)
Text_3 = tk.Text(window, height=2, width=30)
Text_3.place(x=90, y=270)
def confirm_3():
    tmp_string = Text_3.get("1.0", "end")
    print (tmp_string)
Button_3 = tk.Button(window, text='confirm', command=confirm_3)
Button_3.place(x=350, y=270)

tk.Label(window, text=unichr(0x394)+':', font=('Arial', 12)).place(x=60, y=310)
Text_4 = tk.Text(window, height=2, width=30)
Text_4.place(x=90, y=310)
def confirm_4():
    tmp_string = Text_4.get("1.0", "end")
    print (tmp_string)
Button_4 = tk.Button(window, text='confirm', command=confirm_4)
Button_4.place(x=350, y=310)
# "--------------------------"


# "---------2. Simulate Automata-----------------"
tk.Label(window, text='2. Simulate automaton', font=('Arial', 12)).place(x=30, y=360)
tk.Label(window, text='Input the tree:', font=('Arial', 12)).place(x=60, y=400)
Text_5 = tk.Text(window, height=2, width=30)
Text_5.place(x=90, y=440)
def confirm_5():
    tmp_string = Text_5.get("1.0", "end")
    print (tmp_string)
Button_5 = tk.Button(window, text='confirm', command=confirm_5)
Button_5.place(x=350, y=440)
# "--------------------------"

# "---------3. Transition graph-----------------"
tk.Label(window, text='3. Transition graph', font=('Arial', 12)).place(x=30, y=500)
Text_6 = tk.Text(window, height=8, width=30)
Text_6.place(x=90, y=540)

def display():
    tmp_string = Text_6.get("1.0", "end")
    print (tmp_string)
Button_6 = tk.Button(window, text='display', command=display)
Button_6.place(x=350, y=540)
# "--------------------------"

window.mainloop()


