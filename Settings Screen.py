##Settings Screen

##ADD SETTINGS - SCREEN SIZE, THEME, ADD WORD, MUSIC

#Importing required functions
from tkinter import *
from tkinter import ttk
from functools import partial

#Backgrounds
settings_bg = "#AAA3F8"
white_colour = "#ffffff"

#Fonts
title_txt = ("Cooper Black", "50")
title_colour = "#f0f6f7"

class Setting:
    def __init__(self, master):
        
        #Designing frame
        self.master = master
        self.master.title("Hangman Game - Settings")
        self.master.geometry("1000x750+200+100")    
        self.master.configure(bg = settings_bg)       
        self.settings_frame = Frame(self.master, bg = settings_bg)
        self.settings_frame.pack()
        
        #Title
        self.Title = Label(self.settings_frame, text = "Hangman Game", font = title_txt, bg = settings_bg, fg = title_colour)
        ##self.Title.grid(row = 0, column = 0, columnspan = 2, pady = 40)        
        self.Title.pack(side = TOP, fill = BOTH, expand = 1)
        
        #Creating a canvas
        self.the_canvas = Canvas(self.settings_frame, width = 900, height = 800)
        ##the_canvas.grid(row = 2, column = 0, columnspan = 2)
        self.the_canvas.pack(side = LEFT, fill = BOTH, expand = 1, pady =20)
        
        #Adding scrollbar to the canvas
        self.the_scrollbar = ttk.Scrollbar(self.settings_frame, orient = VERTICAL, command = self.the_canvas.yview)
        ##the_scrollbar.grid(row = 2, column = 3, rowspan = 3)
        self.the_scrollbar.pack(side = RIGHT, fill = Y, pady =20)
        
        #Configuring the canvas
        self.the_canvas.configure(yscrollcommand = self.the_scrollbar.set)
        self.the_canvas.bind('<Configure>', lambda e: self.the_canvas.configure(scrollregion = self.the_canvas.bbox("all")))
        
        #Creating another frame in the canvas
        self.inner_frame = Frame(self.the_canvas)
        
        #Add that new frame to a window in the canvas
        self.the_canvas.create_window((0,0), window = self.inner_frame, anchor = 'nw')
        
        
        for thing in range(100):
            self.buttons = Button(self.inner_frame, text = f'button {thing} Yo!')
            self.buttons.grid(row=thing, column = 0, pady= 10, padx=10)
        
        self.my_label = Label(self.inner_frame, text = "it's friday yo!")
        self.my_label.grid(row = 3, column =2)        
        
        

#The main routine
if __name__ == "__main__":
    root = Tk()
    application = Setting(root)
    root.mainloop()