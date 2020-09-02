##Main Screen

##COMPLETE USER LABEL AND THE DIFFERENT BUTTONS

#Importing required functions
from tkinter import *
from functools import partial

#Lists/Dictionaries
current_player = ["LUCIO", "DVA", "0"]
highscore_list = [['DVA', 'NERFTHIS', '3'], ['ASHE', 'BOB', '5'], ['WINSTON', 'BANANAS', '3'], ['MERCY', 'GENJI', '4']]

#Backgrounds
main_bg = "#F76BA4"

#Colours
white_colour = "#ffffff"

#Fonts
title_txt = ("Cooper Black", "50")
title_colour = "#f0f6f7"
login_txt = ("Arial", "30", "bold")
login_colour = "#000000"
userlabel_txt = ("Arial", "20", "bold")
logoutbutton_txt = ("Arial", "18", "underline")

#Startup/Login
class Startup:

    def __init__(self, master):
        
        #Designing frame
        self.master = master
        self.master.title("Hangman Game - Login")
        self.master.geometry("1000x750+200+100")    
        self.master.configure(bg = startup_bg)       
        self.login_frame = Frame(self.master, bg = startup_bg)
        self.login_frame.pack()
         


class Mainscreen:
    
    def __init__(self, master):
        
        #Designing frame
        self.master = master
        self.master.title("Hangman Game - Main Menu")
        self.master.geometry("1000x750+200+100")    
        self.master.configure(bg = main_bg)       
        self.mainscreen_frame = Frame(self.master, bg = main_bg)
        self.mainscreen_frame.pack()    
        
        #If user press cross at top, close mainscreen definition runs...
        self.master.protocol('WM_DELETE_WINDOW', partial(self.close_mainscreen)) 
        
        
        #Title
        self.Title = Label(self.mainscreen_frame, text = "Hangman Game", font = title_txt, bg = main_bg, fg = title_colour)
        self.Title.grid(row = 0, column = 0, pady = 40, padx = 20)  
        
        #User onscreen frame
        self.UserFrame = LabelFrame(self.mainscreen_frame, width = 220, height = 10, font = login_txt, relief = 'ridge', bg = white_colour, bd = 5)
        self.UserFrame.grid(row = 0, column = 3, padx = 60) 
        
        #User Label
        self.Userlabel = Label(self.UserFrame, text =current_player[0], font = userlabel_txt, bg = white_colour, fg = login_colour)
        self.Userlabel.grid(row=0, column=0)  
        
        #Log out button
        self.logout = Button(self.UserFrame, text = "Log Out", font = logoutbutton_txt, bg = white_colour, fg = login_colour, command = self.logout)
        self.logout.grid(row = 1, column = 0)
        
        #Main Options Frame
        self.OptionsFrame = LabelFrame(self.mainscreen_frame, width = 800, height = 800, font = login_txt, relief = 'ridge', bg = main_bg, bd =0)
        self.OptionsFrame.grid(row = 1, column = 0, rowspan = 2) 
        
        #Play button
        self.playbutton = Button(self.OptionsFrame, text = "Play", font = title_txt, bg = white_colour, fg = login_colour, command = self.chosen_play)
        self.playbutton.grid(row = 0, column = 0, pady = 10)
        
        #Help button
        self.helpbutton = Button(self.OptionsFrame, text = "Help", font = title_txt, bg = white_colour, fg = login_colour, command = self.chosen_help)
        self.helpbutton.grid(row = 1, column = 0, pady = 10)
        
        #Setting button
        self.settingsbutton = Button(self.OptionsFrame, text = "Settings", font = title_txt, bg = white_colour, fg = login_colour, command = self.chosen_settings)
        self.settingsbutton.grid(row = 2, column = 0, pady = 10)        
        
        #Highscores frame
        self.HighscoreFrame = LabelFrame(self.mainscreen_frame, width = 400, height = 400, font = login_txt, relief = 'ridge', bg = white_colour, bd =0)
        self.HighscoreFrame.grid(row = 1, column = 3, rowspan = 2)   
        
        #Displaying highscores
        highscore_list.sort(key=lambda e: e[2], reverse=True) 
        
        #self.highscore_headings = Label(self.HighscoreFrame, text ="Position | Name      \t\t |Score\n-----------------------------------", bg = white_colour, fg = login_colour)
        #self.highscore_headings.grid(row=0, column=0) 
        
        self.hslabel_position = Label(self.HighscoreFrame, text ="Position", bg = white_colour, fg = login_colour)
        self.hslabel_position.grid(row=0, column=0)    
        
        self.hslabel_name = Label(self.HighscoreFrame, text ="Name", bg = white_colour, fg = login_colour)
        self.hslabel_name.grid(row=0, column=1)
        
        self.hslabel_score = Label(self.HighscoreFrame, text ="Score", bg = white_colour, fg = login_colour)
        self.hslabel_score.grid(row=0, column=2)    
        
        self.hslabel_design = Label(self.HighscoreFrame, text ="-----------------------------------", bg = white_colour, fg = login_colour)
        self.hslabel_design.grid(row=1, column=0, columnspan = 3)        
        
        for i in range(len(highscore_list)):
            #self.highscores = Label(self.HighscoreFrame, text = ((i+1), highscore_list[i][0], highscore_list[i][2]), bg = white_colour, fg = login_colour)
            #self.highscores.grid(row=(2+i), column=0)       
            
            self.hs_position = Label(self.HighscoreFrame, text = (i+1), bg = white_colour, fg = login_colour)
            self.hs_position.grid(row=(2+i), column=0)
            
            self.hs_name = Label(self.HighscoreFrame, text = highscore_list[i][0], bg = white_colour, fg = login_colour)
            self.hs_name.grid(row=(2+i), column=1) 
            
            self.hs_score = Label(self.HighscoreFrame, text = highscore_list[i][2], bg = white_colour, fg = login_colour)
            self.hs_score.grid(row=(2+i), column=2)             
        
        
    
    def close_mainscreen(self):
        self.master.destroy() 
    
    def logout(self):
        ##save player score and everything.
        
        #Removing from current player
        current_player.clear()
        print(current_player)
        
        #New Routine created
        self.master.destroy() 
        newroot = Tk()
        application = Startup(newroot)
        newroot.mainloop()     
        
    def chosen_play(self):
        
        print("play")
        
        #New Routine created
        ##self.master.destroy() 
        ##newroot = Tk()
        ##application = Startup(newroot)
        ##newroot.mainloop()          
        
    
    def chosen_help(self):
        
        print("help")
        
        #New Routine created
        ##self.master.destroy() 
        ##newroot = Tk()
        ##application = Startup(newroot)
        ##newroot.mainloop()        
    
    def chosen_settings(self):
        
        print("settings")
        
        #New Routine created
        ##self.master.destroy() 
        ##newroot = Tk()
        ##application = Startup(newroot)
        ##newroot.mainloop()        

#The main routine
if __name__ == "__main__":
    root = Tk()
    application = Mainscreen(root)
    root.mainloop()