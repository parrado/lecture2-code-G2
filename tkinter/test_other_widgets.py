from tkinter import *

class SampleApp(Tk):

    def __init__(self):
        super().__init__()

        self.title("Widgets Example")

        # Para impedir cambio de tamaño de la ventana
        self.resizable(False, False)

        self.listBox=Listbox()        
        self.listBox.insert(0, "Python","Java","Kotlin","Rust")
        self.listBox.grid(row=0,column=0,rowspan=4)

        self.var = StringVar()
        self.var.set('French')

        self.rb1=Radiobutton(text='English', variable=self.var, value='English')
        self.rb1.grid(row=0,column=1)
        self.rb2=Radiobutton(text='German', variable=self.var, value='German')
        self.rb2.grid(row=1,column=1)
        self.rb3=Radiobutton(text='French', variable=self.var, value='French')
        self.rb3.grid(row=2,column=1)

        self.canvas=Canvas(bg='white')
        self.canvas.grid(row=4,column=0,rowspan=3,columnspan=2)
        
        
        self.drawCircle()

    def drawCircle(self):
        self.canvas.create_oval(self.canvas.winfo_reqwidth()/2-50, self.canvas.winfo_reqheight()/2-50, self.canvas.winfo_reqwidth()/2+50, self.canvas.winfo_reqheight()/2+50,fill="red")
        
    

        

app = SampleApp()
app.mainloop()



