
# pip install pillow
from PIL import Image, ImageTk
from tkinter import Tk,Canvas,Button,BOTH,DISABLED,NORMAL


# TestWheel class
class TestWheel(Tk):
    def __init__(self,width,height):
        super().__init__()
        self.title("Wheel Example")
        self.resizable(False, False)

        self.button=Button(text="Start",command=self.onClick)
        self.button.pack(pady=20)

        self.canvas = Canvas()
        self.canvas.pack()

        # Load the original image
        img = Image.open("roulette.png")
        self.img=img.resize((int(width/2),int(height/2)))
        self.tk_img = ImageTk.PhotoImage(self.img)
        self.canvas.create_image(int(self.canvas.winfo_reqwidth()/2), int(self.canvas.winfo_reqheight()/2), image=self.tk_img)

        # Number of iterations
        self.Nr=100

        # Rotation angle for each iteration
        self.angle=10
        

    def onClick(self):

        self.button.config(state=DISABLED)
        self.i=0.0
        self.spin_wheel()




    def spin_wheel(self):     
        

        # Number of rotations
        if self.i == self.Nr: 
            self.button.config(state=NORMAL)
            return

        # Rotate original image
        rotated_img = self.img.rotate(self.angle*self.i)
        self.tk_img = ImageTk.PhotoImage(rotated_img)
        

        # Update canvas with rotated image
        self.canvas.delete("all")
        self.canvas.create_image(int(self.canvas.winfo_reqwidth()/2), int(self.canvas.winfo_reqheight()/2), image=self.tk_img)

        # Increment iterations counter
        self.i+=1

        # Animation by calling after
        self.after(33, self.spin_wheel)




# Create TestWheel object
app=TestWheel(500,500)
app.mainloop()

