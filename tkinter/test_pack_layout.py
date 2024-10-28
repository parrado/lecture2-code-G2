import tkinter as tk



class SampleApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pack layout example")         
        self.geometry("320x240")     

        # Crea un Frame
        self.frame = tk.Frame()
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.bottomframe = tk.Frame()
        self.bottomframe.pack(fill=tk.BOTH, expand=True,side = tk.BOTTOM )

        # El widget parent de los tres botones es frame
        self.redbutton = tk.Button(self.frame,text="Red", fg="red")
        self.redbutton.pack( side = tk.RIGHT)

        self.brownbutton = tk.Button(self.frame,text="Brown", fg="brown")
        self.brownbutton.pack( side = tk.RIGHT )

        self.bluebutton = tk.Button(self.frame,text="Blue", fg="blue")
        self.bluebutton.pack( side = tk.RIGHT)

        # El widget padre de los botones negro y verde es bottomframe
        self.blackbutton = tk.Button(self.bottomframe, text="Black", fg="black")
        self.blackbutton.pack(fill=tk.BOTH, expand=True,side=tk.BOTTOM)
        self.greenbutton = tk.Button(self.bottomframe,text="Green", fg="green")
        self.greenbutton.pack(fill=tk.BOTH, expand=True ,side=tk.BOTTOM)
        

app = SampleApp()
app.mainloop()



