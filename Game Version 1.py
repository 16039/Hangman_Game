##Name: 
##Date Finished: 2020
##Information: 
##Created By: Harashi Dev 13YB

##Importing required functions:
from tkinter import *
from functools import partial
import pygame
import math
import random

##Lists/Dictionaries:
players_information = {} #All saved usernames and passwords and scores are appended into this dictionary.
highscores_list = [] #List to deal with highscores and sorting.
current_player = [] #The information for the current player is stored in this list.
game_images = [] #Images for the game is stored in this list
letters = [] #
words_dict = {} #Words and their hint are stored in this list together.
appending_word = [] #List to store a new word and it's hint to append.
guessed = [] #

##Colours:
white_colour = "#ffffff"
black_colour = "#000000"
lightblue_colour = "#c0d6e4"
startup_bg = "#669db3" ##NEED TO CHANGE THE NAME
pygame_white = (255, 255, 255)
pygame_black =(0, 0, 0)


##Fonts:
title_txt = ("Cooper Black", "50") ##NEED TO CHANGE 
login_txt = ("Arial", "30", "bold") ##NEED TO CHANGE

##Loading in images:
#for i in range(7):
    #each_image = pygame.image.load("game_image_" + str(i) + ".png")
    #game_images.append(each_image) 

##Loading in text files:


##Classes:

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
        self.Title = Label(self.mainscreen_frame, text = "Hangman Game", font = title_txt, bg = main_bg, fg = white_colour)
        self.Title.grid(row = 0, column = 0, pady = 40, padx = 20)  
        
        #User onscreen frame
        self.UserFrame = LabelFrame(self.mainscreen_frame, width = 220, height = 10, font = login_txt, relief = 'ridge', bg = 'cadet blue', bd = 5)
        self.UserFrame.grid(row = 0, column = 3, padx = 60) 
        
        #User Label
        self.Userlabel = Label(self.UserFrame, text =current_player[0], font = userlabel_txt, bg = 'cadet blue', fg = login_colour)
        self.Userlabel.grid(row=0, column=0)  
        
        #Log out button
        self.logout = Button(self.UserFrame, text = "Log Out", font = logoutbutton_txt, bg = 'cadet blue', fg = login_colour, command = self.logout)
        self.logout.grid(row = 1, column = 0)
        
        #Main Options Frame
        self.OptionsFrame = LabelFrame(self.mainscreen_frame, width = 800, height = 800, font = login_txt, relief = 'ridge', bg = 'cadet blue', bd = 5)
        self.OptionsFrame.grid(row = 1, column = 0, rowspan = 2) 
        
        #Play button
        self.playbutton = Button(self.OptionsFrame, text = "Play", font = title_txt, bg = 'cadet blue', fg = login_colour, command = self.chosen_play)
        self.playbutton.grid(row = 0, column = 0, pady = 10)
        
        #Help button
        self.helpbutton = Button(self.OptionsFrame, text = "Help", font = title_txt, bg = 'cadet blue', fg = login_colour, command = self.chosen_help)
        self.helpbutton.grid(row = 1, column = 0, pady = 10)
        
        #Setting button
        self.settingsbutton = Button(self.OptionsFrame, text = "Settings", font = title_txt, bg = 'cadet blue', fg = login_colour, command = self.chosen_settings)
        self.settingsbutton.grid(row = 2, column = 0, pady = 10)        
        
        #Highscores frame
        self.HighscoreFrame = LabelFrame(self.mainscreen_frame, width = 400, height = 400, font = login_txt, relief = 'ridge', bg = 'cadet blue', bd = 5)
        self.HighscoreFrame.grid(row = 1, column = 3, rowspan = 2)   
        
        #Displaying highscores
        
    
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

class Register:
    def __init__(self, master):
        
        #Designing frame
        self.master = master
        self.master.title("Hangman Game - Register")
        self.master.geometry('1000x750+200+100')
        self.master.configure(bg = register_bg)
        self.register_frame = Frame(self.master, bg = register_bg)
        self.register_frame.pack()    
        
        #If user press cross at top, close register definition runs...
        self.master.protocol('WM_DELETE_WINDOW', partial(self.close_register))        
        
        #Title
        self.Title = Label(self.register_frame, text = "Hangman Game", font = title_txt, bg = register_bg, fg = white_colour)
        self.Title.grid(row = 0, column = 0, columnspan = 2, pady = 40)    
        
        #Welcome text
        self.Welcometxt = Label(self.register_frame, font = login_txt, text = "Welcome New User!", bg = register_bg, fg = white_colour)
        self.Welcometxt.grid(row = 1, column = 0)    
        
        #Information text
        self.Infotxt = Label(self.register_frame, font = login_txt, text = "Please fill in the details below to start playing:", bg = register_bg, fg = white_colour)
        self.Infotxt.grid(row = 2, column = 0)  
        
        #Register frame
        self.RegisterFrame = LabelFrame(self.register_frame, width = 550, height = 300, font = login_txt, relief = 'ridge', bg = 'cadet blue', bd =20)
        self.RegisterFrame.grid(row = 3, column = 0, pady = 10)
        
        #Button frame
        self.Buttonframe = LabelFrame(self.register_frame, width = 550, height = 100, font = login_txt, relief = 'ridge', bg = 'cadet blue', bd = 20)
        self.Buttonframe.grid(row = 4, column = 0, pady = 10)
        
        #Username label
        self.labelUsername = Label(self.RegisterFrame, text ='Choose a Username', font = login_txt,
                                 bd = 22, bg = 'cadet blue', fg = white_colour)
        self.labelUsername.grid(row=0, column=0)
        
        #Username entry
        self.entryUsername = Entry(self.RegisterFrame, font = login_txt)
        self.entryUsername.grid(row=0, column=1, padx = 10)
        
        #Password label
        self.labelPassword = Label(self.RegisterFrame, text ='Choose a Password', font = login_txt,
                                 bd = 22, bg = 'cadet blue', fg = white_colour)
        self.labelPassword.grid(row=1, column=0)        
        
        #Password entry
        self.entryPassword = Entry(self.RegisterFrame, font = login_txt)
        self.entryPassword.grid(row=1, column=1, padx = 10)  
        
        #Register button
        self.buttonLogin = Button(self.Buttonframe, text = 'Register!', font = login_txt, width = 17, command = self.registerUser)
        self.buttonLogin.grid(row = 3, column = 0, pady = 8, padx = 8)
              
        
    def registerUser(self):
        
        newuser = self.entryUsername.get()
        newpass = self.entryPassword.get()
        
        #for key in player_info.keys():
        if newuser.upper() in player_info:
            #Error message appears
            self.error = Label(self.register_frame, font = login_txt, text = "Username is taken!", bg = white_colour, fg = 'Red')
            self.error.grid(row = 5, column = 0)   
            root.after(1500, self.error.destroy)  

        else:
            if re.search(r'[\s]', newuser) or re.search(r'[\s]', newpass):
                self.error = Label(self.register_frame, font = login_txt, text = "No spaces are allowed!", bg = white_colour, fg = 'Red')
                self.error.grid(row = 5, column = 0)   
                root.after(1500, self.error.destroy) 
                
            else:
                if newuser == "" or newpass == "":
                    self.error = Label(self.register_frame, font = login_txt, text = "Please fill in all details!", bg = white_colour, fg = 'Red')
                    self.error.grid(row = 5, column = 0)   
                    root.after(1500, self.error.destroy) 
                
                else:
                    current_player.append(theuser.upper())
                    current_player.append(thepass.upper())
                    print(current_player)                         
                    self.close_register()
        
        
        
    def close_register(self):
        self.master.destroy()  
        root = Tk()
        application = Startup(root)
        root.mainloop()

class Startup:
    
    def registerWindow(self):
        
        #New Routine created
        self.master.destroy() 
        newroot = Tk()
        application = Register(newroot)
        newroot.mainloop()        
        
    
    def login(self):
        
        #Checks if both username and password entered are correct
        theuser = self.entryUsername.get()
        thepass = self.entryPassword.get()
        for key, value in player_info.items():
            if key == theuser.upper() and value == thepass.upper():
                
                #Appending user information into current player list
                current_player.append(theuser.upper())
                current_player.append(thepass.upper())
                print(current_player) 
                
                #New routine created
                root.destroy() 
                newroot = Tk()
                application = Mainscreen(newroot)
                newroot.mainloop()
                
            else:
                #Error message appears
                self.error = Label(self.login_frame, font = login_txt, text = "Username or password incorrect!", bg = startup_bg, fg = 'Red')
                self.error.grid(row = 5, column = 0)   
                root.after(1500, self.error.destroy)

    def __init__(self, master):
        
        #Designing frame
        self.master = master
        self.master.title("Hangman Game - Login")
        self.master.geometry("1000x750+200+100")    
        self.master.configure(bg = startup_bg)       
        self.login_frame = Frame(self.master, bg = startup_bg)
        self.login_frame.pack()
        
        #Title
        self.Title = Label(self.login_frame, text = "Hangman Game", font = title_txt, bg = startup_bg, fg = white_colour)
        self.Title.grid(row = 0, column = 0, columnspan = 2, pady = 40)
        
        #Login frame
        self.LoginFrame = LabelFrame(self.login_frame, width = 550, height = 300, font = login_txt, relief = 'ridge', bg = 'cadet blue', bd =20)
        self.LoginFrame.grid(row = 1, column = 0)
        
        #Button frame
        self.Buttonframe = LabelFrame(self.login_frame, width = 550, height = 100, font = login_txt, relief = 'ridge', bg = 'cadet blue', bd = 20)
        self.Buttonframe.grid(row = 2, column = 0, pady = 20) 
        
        #Username label
        self.labelUsername = Label(self.LoginFrame, text ='Username', font = login_txt,
                                 bd = 22, bg = 'cadet blue', fg = white_colour)
        self.labelUsername.grid(row=0, column=0)
        
        #Username entry
        self.entryUsername = Entry(self.LoginFrame, font = login_txt)
        self.entryUsername.grid(row=0, column=1, padx = 10)
        
        #Password label
        self.labelPassword = Label(self.LoginFrame, text ='Password', font = login_txt,
                                 bd = 22, bg = 'cadet blue', fg = white_colour)
        self.labelPassword.grid(row=1, column=0)        
        
        #Password entry
        self.entryPassword = Entry(self.LoginFrame, font = login_txt, show = '*')
        self.entryPassword.grid(row=1, column=1, padx = 10)  
        
        #Login button
        self.buttonLogin = Button(self.Buttonframe, text = 'Login', font = login_txt, width = 17, command = self.login)
        self.buttonLogin.grid(row = 3, column = 0, pady = 8, padx = 8)
        
        #Register button
        self.buttonRegister = Button(self.Buttonframe, text = 'Register', font = login_txt, width = 17, command = self.registerWindow)
        self.buttonRegister.grid(row = 4, column = 0, pady = 8, padx = 8) 


##Starting Routine:
if __name__ == "__main__":
    root = Tk()
    application = Startup(root)
    root.mainloop()