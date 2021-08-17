import Tkinter as tk
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
