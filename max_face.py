import Tkinter as tk
from treeautomaton import *

class max_face():

    def __init__(self,master):
        self.master= master
        self.master.resizable(0,0)
        self.master.geometry('1536x841+0+0')
        self.defaultbg = master.cget('bg')
        # "---------1. Create Automata-----------------"
        self.label_1 = tk.Label(self.master, text='1. Create automaton', font=('Arial', 12))
        
        self.label_2 = tk.Label(self.master, text='F:', font=('Arial', 12))

        self.frm_5 = tk.Frame(self.master)
        self.scrollbar_5 = tk.Scrollbar(self.frm_5)
        self.Text_1 = tk.Text(self.frm_5, height=9, width=50, yscrollcommand=self.scrollbar_5.set)

        self.Button_1 = tk.Button(self.master, text='confirm', command=self.confirm_1)

        self.Button_12 = tk.Button(self.master, text='clear', command=self.clear_12)

        self.label_3 = tk.Label(self.master, text='Q:', font=('Arial', 12))

        self.frm_4 = tk.Frame(self.master)

        self.scrollbar_4 = tk.Scrollbar(self.frm_4)
        self.Text_2 = tk.Text(self.frm_4, height=9, width=50, yscrollcommand=self.scrollbar_4.set)


        self.Button_2 = tk.Button(self.master, text='confirm', command=self.confirm_2)

        self.Button_11 = tk.Button(self.master, text='clear', command=self.clear_11)


        self.label_4 = tk.Label(self.master, text='Qf:', font=('Arial', 12))

        self.frm_3 = tk.Frame(self.master)

        self.scrollbar_3 = tk.Scrollbar(self.frm_3)
        self.Text_3 = tk.Text(self.frm_3, height=9, width=50, yscrollcommand=self.scrollbar_3.set)


        self.Button_3 = tk.Button(self.master, text='confirm', command=self.confirm_3)


        self.Button_10 = tk.Button(self.master, text='clear', command=self.clear_10)


        self.label_5 = tk.Label(self.master, text=unichr(0x394)+':', font=('Arial', 12))

        self.frm_2 = tk.Frame(self.master)

        self.scrollbar_2 = tk.Scrollbar(self.frm_2)
        self.Text_4 = tk.Text(self.frm_2, height=9, width=50, yscrollcommand=self.scrollbar_2.set)


        self.Button_4 = tk.Button(self.master, text='confirm', command=self.confirm_4)


        self.Button_9 = tk.Button(self.master, text='clear', command=self.clear_9)

        # "--------------------------"

        # "---------2. Simulate Automata-----------------"
        self.label_6 = tk.Label(self.master, text='2. Simulate automaton', font=('Arial', 12))

        self.label_7 = tk.Label(self.master, text='Input the tree:', font=('Arial', 12))


        self.Text_5 = tk.Text(self.master, height=2, width=40)


        self.Button_5 = tk.Button(self.master, text='confirm', command=self.confirm_5)


        self.Button_8 = tk.Button(self.master, text='clear', command=self.clear_8)

        # "--------------------------"

        # "---------3. Transition graph-----------------"
        self.label_8 = tk.Label(self.master, text='3. Transition graph', font=('Arial', 12))


        self.frm_1 = tk.Frame(self.master)


        self.scrollbar_1 = tk.Scrollbar(self.frm_1)
        self.Text_6 = tk.Text(self.frm_1, height=10, width=60, yscrollcommand=self.scrollbar_1.set)

        self.Button_6 = tk.Button(self.master, text='display', command=self.display)

        self.Button_7 = tk.Button(self.master, text='clear', command=self.clear_7)

        # "--------------------------"

        # "---------Button continue-----------------"
        self.Continue_1 = tk.Button(self.master, text='continue', command = self.continue_1)
        self.Continue_2 = tk.Button(self.master, text='continue', command = self.continue_2)
        self.Continue_3 = tk.Button(self.master, text='continue', command = self.continue_3)
        self.Continue_4 = tk.Button(self.master, text='continue', command = self.continue_4)
        self.Continue_5 = tk.Button(self.master, text='continue', command = self.continue_5)

        # "--------------------------"

        self.create_face()

    def create_face(self):
        self.label_1.place(x=30, y=150)
        self.label_2.place(x=180, y=190)
        self.frm_5.place(x=200, y=190)
        self.scrollbar_5.config(command=self.Text_1.yview)
        self.scrollbar_5.pack(side='right', fill='y')
        self.Text_1.pack(side="left")
        self.Button_1.place(x=630, y=190)
        self.Button_12.place(x=690, y=190)

        self.Continue_1.place(x=735, y=190)

        self.label_3.place(x=820, y=190)
        self.frm_4.place(x=850, y=190)
        self.scrollbar_4.config(command=self.Text_2.yview)
        self.scrollbar_4.pack(side='right', fill='y')
        self.Text_2.pack(side="left")
        self.Button_2.place(x=1280, y=190)
        self.Button_11.place(x=1340, y=190)
        self.Continue_2.place(x=1385, y=190)
        
        self.label_4.place(x=175, y=360)
        self.frm_3.place(x=200, y=360)
        self.scrollbar_3.config(command=self.Text_3.yview)
        self.scrollbar_3.pack(side='right', fill='y')
        self.Text_3.pack(side="left")
        self.Button_3.place(x=630, y=360)
        self.Button_10.place(x=690, y=360)
        self.Continue_3.place(x=735, y=360)
        
        self.label_5.place(x=820, y=360)
        self.frm_2.place(x=850, y=360)
        self.scrollbar_2.config(command=self.Text_4.yview)
        self.scrollbar_2.pack(side='right', fill='y')
        self.Text_4.pack(side="left")
        self.Button_4.place(x=1280, y=360)
        self.Button_9.place(x=1340, y=360)
        self.Continue_4.place(x=1385, y=360)


        self.label_6.place(x=30, y=530)
        self.label_7.place(x=180, y=560)
        self.Text_5.place(x=290, y=570)

        self.Button_5.place(x=620, y=570)
        self.Button_8.place(x=680, y=570)
        self.Continue_5.place(x=725, y=570)

        self.label_8.place(x=30, y=610)
        self.frm_1.place(x=200, y=635)
        self.scrollbar_1.config(command=self.Text_6.yview)
        self.scrollbar_1.pack(side='right', fill='y')
        self.Text_6.pack(side="left")
        self.Text_6.config(state='disabled')
        self.Button_6.place(x=725, y=635)
        self.Button_7.place(x=725, y=675)

    def destroy(self):
        self.label_1.destroy()
        self.label_2.destroy()
        self.frm_5.destroy()
        self.Button_1.destroy()
        self.Button_12.destroy()
        self.Continue_1.destroy()
        self.label_3.destroy()
        self.frm_4.destroy()
        self.Button_2.destroy()
        self.Button_11.destroy()
        self.Continue_2.destroy()
        self.label_4.destroy()
        self.frm_3.destroy()
        self.Button_3.destroy()
        self.Button_10.destroy()
        self.Continue_3.destroy()
        self.label_5.destroy()
        self.frm_2.destroy()
        self.Button_4.destroy()
        self.Button_9.destroy()
        self.Continue_4.destroy()
        self.label_6.destroy()
        self.label_7.destroy()
        self.Text_5.destroy()
        self.Button_5.destroy()
        self.Button_8.destroy()
        self.Continue_5.destroy()
        self.label_8.destroy()
        self.frm_1.destroy()
        self.Button_6.destroy()
        self.Button_7.destroy()


    def confirm_1(self):
        tmp_string = self.Text_1.get("1.0", "end")
        file = open('operator.txt','w')
        file.write(tmp_string)
        file.close()
        self.Button_1.config(state='disabled', bg='black')
        self.Text_1.config(state='disabled')

    def clear_12(self):
        self.Text_1.config(state='normal')
        self.Text_1.delete('1.0','end')
        self.Button_1.config(state='normal', bg=self.defaultbg)

    def continue_1(self):
        self.Button_1.config(state='normal', bg=self.defaultbg)
        self.Text_1.config(state='normal')

    def confirm_2(self):
        tmp_string = self.Text_2.get("1.0", "end")
        file = open('states.txt','w')
        file.write(tmp_string)
        file.close()
        self.Button_2.config(state='disabled', bg='black')
        self.Text_2.config(state='disabled')

    def clear_11(self):
        self.Text_2.config(state='normal')
        self.Text_2.delete('1.0','end')
        self.Button_2.config(state='normal', bg=self.defaultbg)

    def continue_2(self):
        self.Button_2.config(state='normal', bg=self.defaultbg)
        self.Text_2.config(state='normal')

    def confirm_3(self):
        tmp_string = self.Text_3.get("1.0", "end")
        file = open('finalsymbols.txt','w')
        file.write(tmp_string)
        file.close()
        self.Button_3.config(state='disabled', bg='black')
        self.Text_3.config(state='disabled')

    def clear_10(self):
        self.Text_3.config(state='normal')
        self.Text_3.delete('1.0','end')
        self.Button_3.config(state='normal', bg=self.defaultbg)

    def continue_3(self):
        self.Button_3.config(state='normal', bg=self.defaultbg)
        self.Text_3.config(state='normal')

    def confirm_4(self):
        tmp_string_1 = self.Text_4.get("1.0", "end")
        file = open('productions.txt','w')
        file.write(tmp_string_1)
        file.close()
        self.Button_4.config(state='disabled', bg='black')
        self.Text_4.config(state='disabled')

    def clear_9(self):
        self.Text_4.config(state='normal')
        self.Text_4.delete('1.0','end')
        self.Button_4.config(state='normal', bg=self.defaultbg)

    def continue_4(self):
        self.Button_4.config(state='normal', bg=self.defaultbg)
        self.Text_4.config(state='normal')

    def confirm_5(self):
        tmp_string = self.Text_5.get("1.0", "end")
        file = open('input_string.txt','w')
        file.write(tmp_string)
        file.close()
        self.Button_5.config(state='disabled', bg='black')
        self.Text_5.config(state='disabled')

    def clear_8(self):
        self.Text_5.config(state='normal')
        self.Text_5.delete('1.0','end')
        self.Button_5.config(state='normal', bg=self.defaultbg)

    def continue_5(self):
        self.Button_5.config(state='normal', bg=self.defaultbg)
        self.Text_5.config(state='normal')

    def lines(self,file_stream):
        for line in file_stream:
            yield line

    def display(self):
        run()
        self.Text_6.config(state='normal')
        for line in lines(open('display.txt','r')):
            self.Text_6.insert('end', line)
        self.Text_6.config(state='disabled')
        self.Button_6.config(state='disabled', bg='black')

    def clear_7(self):
        self.Text_6.config(state='normal')
        self.Text_6.delete('1.0','end')
        self.Text_6.config(state='disabled')
        self.Button_6.config(state='normal', bg=self.defaultbg)

    def clear_all(self):
        self.clear_7()
        self.clear_8()
        self.clear_9()
        self.clear_10()
        self.clear_11()
        self.clear_12()
