from tkinter import *

class SampleApp(Tk):

    def __init__(self):
        super().__init__()

        self.title("Events Example")

        # Para impedir cambio de tamaño de la ventana
        self.resizable(False, False)

        self.listBox=Listbox()        
        self.listBox.insert(0, "Circle","Square","Rectangle","Triangle")
        self.listBox.grid(row=0,column=0,rowspan=4,columnspan=1)

        # Vincula evento
        self.listBox.bind('<<ListboxSelect>>', self.onSelection)

       

        self.canvas=Canvas(bg='white')
        self.canvas.grid(row=4,column=0,rowspan=3,columnspan=1)
        
        
        

    def drawCircle(self):
        self.canvas.create_oval(self.canvas.winfo_reqwidth()/2-50, self.canvas.winfo_reqheight()/2-50, self.canvas.winfo_reqwidth()/2+50, self.canvas.winfo_reqheight()/2+50,fill="red")
    
    def drawSquare(self):
        self.canvas.create_rectangle(self.canvas.winfo_reqwidth()/2-50, self.canvas.winfo_reqheight()/2-50, self.canvas.winfo_reqwidth()/2+50, self.canvas.winfo_reqheight()/2+50,fill="blue")
    
    def drawRectangle(self):
        self.canvas.create_rectangle(self.canvas.winfo_reqwidth()/2-100, self.canvas.winfo_reqheight()/2-50, self.canvas.winfo_reqwidth()/2+100, self.canvas.winfo_reqheight()/2+50,fill="green")

    def drawTriangle(self):
        self.canvas.create_polygon([self.canvas.winfo_reqwidth()/2-100, self.canvas.winfo_reqheight()/2+50, self.canvas.winfo_reqwidth()/2,self.canvas.winfo_reqheight()/2-100,self.canvas.winfo_reqwidth()/2+100, self.canvas.winfo_reqheight()/2+50],fill="orange")
  
    
      
        
    
    def onSelection(self,event):
        #print(event)
        self.canvas.delete("all")
        sel=self.listBox.curselection()
        print(sel)    
        match sel:
            case (0,):
                self.drawCircle()
            case (1,):
                self.drawSquare()
            case (2,):
                self.drawRectangle()
            case (3,):
                self.drawTriangle()


        

app = SampleApp()
app.mainloop()



