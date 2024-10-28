from tkinter import *

class MiApp(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("640x480")
        self.title("Hello World!!!")
        self.label = Label(text="Hello, world" )
        self.label.configure(font=("Arial", 25))

        self.label.pack()

app = MiApp()
app.mainloop()