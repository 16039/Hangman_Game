##Login or Register Screen

##NEED TO WORK ON TXT FILES
##SOME OF THE COLOURS ARE OFF

#Importing required functions
from tkinter import *
from functools import partial

#Lists/Dictionaries
player_info = {'KOOKIE':'KOOKIEKAT', 'DVA':'NERFTHIS', 'ASHE':'BOB'}
current_player = []

#Backgrounds
startup_bg = "#669db3"
register_bg = "#F66E51"
white_colour = "#ffffff"

#Fonts
title_txt = ("Cooper Black", "50")
title_colour = "#f0f6f7"
design1_txt = ("Wingdings 3", "25")
design1_colour = "#f0f6f7"
login_txt = ("Arial", "30", "bold")
login_colour = "#000000"
entry_txt = ("Arial", "30", "bold")
entry_colour = "#000000"

class Mainscreen:
    pass

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
        self.Title = Label(self.register_frame, text = "Hangman Game", font = title_txt, bg = register_bg, fg = title_colour)
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
                    ##current_player.append(theuser.upper())
                    ##current_player.append(thepass.upper())
                    ##print(current_player)                         
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
        self.Title = Label(self.login_frame, text = "Hangman Game", font = title_txt, bg = startup_bg, fg = title_colour)
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
        
#The main routine
if __name__ == "__main__":
    root = Tk()
    application = Startup(root)
    root.mainloop()