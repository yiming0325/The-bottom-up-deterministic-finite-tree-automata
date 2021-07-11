import Tkinter as tk
from treeautomaton import *


class normal_face():

    def __init__(self,master):
        self.master= master
        self.master.resizable(0,0)
        self.master.geometry('650x700+0+0')
        self.defaultbg = master.cget('bg')

        # "---------1. Create Automata-----------------"
        self.label_1 = tk.Label(self.master, text='1. Create automaton', font=('Arial', 12))
        
        self.label_2 = tk.Label(self.master, text='F:', font=('Arial', 12))

        self.frm_5 = tk.Frame(self.master)
        self.scrollbar_5 = tk.Scrollbar(self.frm_5)
        self.Text_1 = tk.Text(self.frm_5, height=3, width=30, yscrollcommand=self.scrollbar_5.set)

        self.Button_1 = tk.Button(self.master, text='confirm', command=self.confirm_1)

        self.Button_12 = tk.Button(self.master, text='clear', command=self.clear_12)

        self.label_3 = tk.Label(self.master, text='Q:', font=('Arial', 12))

        self.frm_4 = tk.Frame(self.master)

        self.scrollbar_4 = tk.Scrollbar(self.frm_4)
        self.Text_2 = tk.Text(self.frm_4, height=3, width=30, yscrollcommand=self.scrollbar_4.set)


        self.Button_2 = tk.Button(self.master, text='confirm', command=self.confirm_2)

        self.Button_11 = tk.Button(self.master, text='clear', command=self.clear_11)


        self.label_4 = tk.Label(self.master, text='Qf:', font=('Arial', 12))

        self.frm_3 = tk.Frame(self.master)

        self.scrollbar_3 = tk.Scrollbar(self.frm_3)
        self.Text_3 = tk.Text(self.frm_3, height=3, width=30, yscrollcommand=self.scrollbar_3.set)


        self.Button_3 = tk.Button(self.master, text='confirm', command=self.confirm_3)


        self.Button_10 = tk.Button(self.master, text='clear', command=self.clear_10)


        self.label_5 = tk.Label(self.master, text=unichr(0x394)+':', font=('Arial', 12))

        self.frm_2 = tk.Frame(self.master)

        self.scrollbar_2 = tk.Scrollbar(self.frm_2)
        self.Text_4 = tk.Text(self.frm_2, height=3, width=30, yscrollcommand=self.scrollbar_2.set)


        self.Button_4 = tk.Button(self.master, text='confirm', command=self.confirm_4)


        self.Button_9 = tk.Button(self.master, text='clear', command=self.clear_9)

        # "--------------------------"

        # "---------2. Simulate Automata-----------------"
        self.label_6 = tk.Label(self.master, text='2. Simulate automaton', font=('Arial', 12))

        self.label_7 = tk.Label(self.master, text='Input the tree:', font=('Arial', 12))


        self.Text_5 = tk.Text(self.master, height=1, width=30)


        self.Button_5 = tk.Button(self.master, text='confirm', command=self.confirm_5)


        self.Button_8 = tk.Button(self.master, text='clear', command=self.clear_8)

        # "--------------------------"

        # "---------3. Transition graph-----------------"
        self.label_8 = tk.Label(self.master, text='3. Transition graph', font=('Arial', 12))


        self.frm_1 = tk.Frame(self.master)


        self.scrollbar_1 = tk.Scrollbar(self.frm_1)
        self.Text_6 = tk.Text(self.frm_1, height=8, width=50, yscrollcommand=self.scrollbar_1.set)

        self.Button_6 = tk.Button(self.master, text='display', command=self.display)

        self.Button_7 = tk.Button(self.master, text='clear', command=self.clear_7)

    # "--------------------------"
        self.create_face()

    def create_face(self):
        self.label_1.place(x=30, y=150)
        self.label_2.place(x=60, y=190)
        self.frm_5.place(x=90, y=190)
        self.scrollbar_5.config(command=self.Text_1.yview)
        self.scrollbar_5.pack(side='right', fill='y')
        self.Text_1.pack(side="left")
        self.Button_1.place(x=360, y=190)
        self.Button_12.place(x=420, y=190)
        self.label_3.place(x=60, y=250)
        self.frm_4.place(x=90, y=250)
        self.scrollbar_4.config(command=self.Text_2.yview)
        self.scrollbar_4.pack(side='right', fill='y')
        self.Text_2.pack(side="left")
        self.Button_2.place(x=360, y=250)
        self.Button_11.place(x=420, y=250)
        self.label_4.place(x=60, y=310)
        self.frm_3.place(x=90, y=310)
        self.scrollbar_3.config(command=self.Text_3.yview)
        self.scrollbar_3.pack(side='right', fill='y')
        self.Text_3.pack(side="left")
        self.Button_3.place(x=360, y=310)
        self.Button_10.place(x=420, y=310)
        self.label_5.place(x=60, y=370)
        self.frm_2.place(x=90, y=370)
        self.scrollbar_2.config(command=self.Text_4.yview)
        self.scrollbar_2.pack(side='right', fill='y')
        self.Text_4.pack(side="left")
        self.Button_4.place(x=360, y=370)
        self.Button_9.place(x=420, y=370)
        self.label_6.place(x=30, y=430)
        self.label_7.place(x=60, y=455)
        self.Text_5.place(x=90, y=485)

        self.Button_5.place(x=350, y=480)
        self.Button_8.place(x=410, y=480)

        self.label_8.place(x=30, y=510)
        self.frm_1.place(x=90, y=540)
        self.scrollbar_1.config(command=self.Text_6.yview)
        self.scrollbar_1.pack(side='right', fill='y')
        self.Text_6.pack(side="left")
        self.Button_6.place(x=515, y=540)
        self.Button_7.place(x=515, y=580)

        """
        self.master.update()
        print(self.master.winfo_width())
        print(self.master.winfo_height())
        """

    def destroy(self):
        self.label_1.destroy()
        self.label_2.destroy()
        self.frm_5.destroy()
        self.Button_1.destroy()
        self.Button_12.destroy()
        self.label_3.destroy()
        self.frm_4.destroy()
        self.Button_2.destroy()
        self.Button_11.destroy()
        self.label_4.destroy()
        self.frm_3.destroy()
        self.Button_3.destroy()
        self.Button_10.destroy()
        self.label_5.destroy()
        self.frm_2.destroy()
        self.Button_4.destroy()
        self.Button_9.destroy()
        self.label_6.destroy()
        self.label_7.destroy()
        self.Text_5.destroy()
        self.Button_5.destroy()
        self.Button_8.destroy()
        self.label_8.destroy()
        self.frm_1.destroy()
        self.Button_6.destroy()
        self.Button_7.destroy()

    def confirm_1(self):
        tmp_string = self.Text_1.get("1.0", "end")
        print (tmp_string)
        self.Button_1.config(state='disabled', bg='black')

    def clear_12(self):
        self.Text_1.delete('1.0','end')
        self.Button_1.config(state='normal', bg=self.defaultbg)

    def confirm_2(self):
        tmp_string = self.Text_2.get("1.0", "end")
        print (tmp_string)
        self.Button_2.config(state='disabled', bg='black')

    def clear_11(self):
        self.Text_2.delete('1.0','end')
        self.Button_2.config(state='normal', bg=self.defaultbg)

    def confirm_3(self):
        tmp_string = self.Text_3.get("1.0", "end")
        file = open('finalsymbols.txt','w')
        file.write(tmp_string)
        file.close()
        self.Button_3.config(state='disabled', bg='black')

    def clear_10(self):
        self.Text_3.delete('1.0','end')
        self.Button_3.config(state='normal', bg=self.defaultbg)

    def confirm_4(self):
        tmp_string_1 = self.Text_4.get("1.0", "end")
        file = open('productions.txt','w')
        file.write(tmp_string_1)
        file.close()
        self.Button_4.config(state='disabled', bg='black')

    def clear_9(self):
        self.Text_4.delete('1.0','end')
        self.Button_4.config(state='normal', bg=self.defaultbg)

    def confirm_5(self):
        tmp_string = self.Text_5.get("1.0", "end")
        file = open('input_string.txt','w')
        file.write(tmp_string)
        file.close()
        self.Button_5.config(state='disabled', bg='black')


    def clear_8(self):
        self.Text_5.delete('1.0','end')
        self.Button_5.config(state='normal', bg=self.defaultbg)

    def lines(self,file_stream):
        for line in file_stream:
            yield line

    def display(self):
        run()
        for line in lines(open('display.txt','r')):
            self.Text_6.insert('end', line)
        self.Button_6.config(state='disabled', bg='black')

    def clear_7(self):
        self.Text_6.delete('1.0','end')
        self.Button_6.config(state='normal', bg=self.defaultbg)
    
    def clear_all(self):
        self.clear_7()
        self.clear_8()
        self.clear_9()
        self.clear_10()
        self.clear_11()
        self.clear_12()
