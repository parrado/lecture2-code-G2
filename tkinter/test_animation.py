from tkinter import *
from random import random
from math import cos,sin

class TestAnimation(Tk):

    def __init__(self):
        super().__init__()

        self.title("Animation Example")

        # Para impedir cambio de tamaño de la ventana
        self.resizable(False, False)

        self.end_button = Button(text="Start",command=self.startAnimation)      
        self.end_button.grid(row=0,column=0,columnspan=2,pady=10)

       

        self.canvas=Canvas(bg='white')
        self.canvas.grid(row=4,column=0,rowspan=3,columnspan=2)
        self.ball_vi_x=0
        self.ball_vi_y=0
        self.ball_x=self.canvas.winfo_reqwidth()/2
        self.ball_y=self.canvas.winfo_reqheight()/2
        self.id=None
        self.isAnimating=False

        
        self.drawBall()
        
        

    def drawBall(self):
        if self.id:
            self.canvas.moveto(self.id,self.ball_x-10,self.ball_y-10)
        else:    
            self.id=self.canvas.create_oval(self.ball_x-10,self.ball_y-10 , self.ball_x+10,self.ball_y+10,fill="red")
    
  
    
      
        
    
    def startAnimation(self):
        if self.ball_vi_x==0 and self.ball_vi_y==0:
            angle=random()*(3.141592654)/4.0+(3.141592654)/4.0
            vi=9
            self.ball_vi_x,self.ball_vi_y=int(vi*cos(angle)),-int(vi*sin(angle))
       
       
        if self.isAnimating==False:
            self.end_button.configure(text="Stop")
            self.isAnimating=True           

        else:            
            self.end_button.configure(text="Start")
            self.isAnimating=False
        
        self.animate()

        

    def animate(self):
        if self.isAnimating:

            if self.ball_x>=(self.canvas.winfo_reqwidth()-10):
                self.ball_vi_x=-self.ball_vi_x

            if self.ball_x<=10:
                self.ball_vi_x=-self.ball_vi_x

            if self.ball_y>=(self.canvas.winfo_reqheight()-10):
                self.ball_vi_y=-self.ball_vi_y

            if self.ball_y<=10:
                self.ball_vi_y=-self.ball_vi_y  

            
            self.ball_x=self.ball_x+self.ball_vi_x
            self.ball_y=self.ball_y+self.ball_vi_y
            self.drawBall()
            
            self.after(33,self.animate)

        


        

app = TestAnimation()
app.mainloop()



