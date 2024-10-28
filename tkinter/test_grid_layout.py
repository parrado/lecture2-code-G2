from tkinter import *

class SampleApp(Tk):
    def __init__(self):
        super().__init__()

        # Para impedir cambio de tamaño de la ventana
        self.resizable(False, False)

        # Creación de dos Labels
        self.l1 = Label(text = "Height")
        self.l2 = Label(text = "Width")

        # Disposición de Labels
        self.l1.grid(row = 0, column = 0, sticky = W, pady = 2)
        self.l2.grid(row = 1, column = 0, sticky = W, pady = 2)

        # Entry widgets
        self.e1 = Entry()
        self.e2 = Entry()

        # Disposición de widgets Entry 
        self.e1.grid(row = 0, column = 1, pady = 2)
        self.e2.grid(row = 1, column = 1, pady = 2)

        # Check button
        self.c1 = Checkbutton(text = "Preserve")
        self.c1.grid(row = 2, column = 0, sticky = W, columnspan = 2)

        # Se crea imagen
        img = PhotoImage(file = "kratos.png")
        self.img1 = img.subsample(5, 5)

        # Label con imagen
        self.imlabel=Label(image = self.img1)
        self.imlabel.grid(row = 0, column = 2,
        columnspan = 2, rowspan = 2, padx = 5, pady = 5)

        # Botones
        self.b1 = Button(text = "Zoom in")
        self.b2 = Button(text = "Zoom out")

        # Disposición de botones
        self.b1.grid(row = 2, column = 2, sticky = E)
        self.b2.grid(row = 2, column = 3, sticky = E)



        

app = SampleApp()
app.mainloop()



