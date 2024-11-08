from tkinter import *
from tkinter import messagebox 



class TestButtonClick(Tk):
    def __init__(self):
        super().__init__()
        self.resizable(False, False)
        self.title("Click button example")
        self.geometry("400x300")     
        # Etiqueta
        self.label=Label(text="Etiqueta")         
        self.label.grid(row=0,column=0,sticky='',pady=10)
        
       # Botón
        self.end_button = Button(text="Botón",command=self.onClick)      
        self.end_button.grid(row=1,column=0,sticky='',pady=10)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)



    def onClick(self):
        messagebox.showinfo("Información","Hola!!")
        self.label.config(text="Texto cambiado")

       

app = TestButtonClick()
app.mainloop()



