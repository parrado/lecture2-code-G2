import tkinter as tk



class SampleApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Place layout Example")
        self.geometry("600x300+200+100")
        # Etiqueta
        self.label=tk.Label(        
        text="Etiqueta en posición absoluta",       
        )
        
        self.label.place(x=200, y=10)

        # Botón
        self.end_button = tk.Button(text="Botón")
        self.end_button.place(x=125, y=250)
       

app = SampleApp()
app.mainloop()



