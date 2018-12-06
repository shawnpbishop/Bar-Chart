#This program is written by Shawn Bishop.

from tkinter import *

class BarGui:
    def __init__(self):
        window = Tk()
        window.title("Bar Chart")

        self.canvas = Canvas(window, bg = "white", width = 500, height = 200)
        self.canvas.pack()
        self.canvas.create_rectangle(20, 140, 120, 180, fill="red")
        self.canvas.create_text(70, 130, text="Projects--20%")
        self.canvas.create_rectangle(140, 160, 240, 180, fill="blue")
        self.canvas.create_text(190, 150, text="Quizzes--10%")
        self.canvas.create_rectangle(260, 120, 360, 180, fill="green")
        self.canvas.create_text(310, 110, text="Midterm--30%")
        self.canvas.create_rectangle(380, 100, 480, 180, fill="orange")
        self.canvas.create_text(430, 90, text="Final--40%")
        self.canvas.create_line(0, 180, 500, 180)


        
        mainloop()


BarGui()
