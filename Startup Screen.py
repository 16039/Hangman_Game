from tkinter import *
from functools import partial

player_info = {'Mr':'Dad', 'Mrs':'Mum', 'Little':'Bird'}
new_player = []
current_player = []


class Startup:
    
    def register(self):
        print("Register session started")
        
        background_colour = "green"
        
        #Disable login and register buttons
        self.login_button.config(state = DISABLED)
        self.register_button.config(state = DISABLED)
        
        #Sets up child window (i.e. register box)
        self.register_box= Toplevel()
        
        #If user press cross at top, closes register and 'unlocks' the login and register buttons...
        self.register_box.protocol('WM_DELETE_WINDOW', partial(self.close_register)) 
        
        #Set up GUI Frame
        self.register_frame = Frame(self.register_box, bg = background_colour, pady = 10)
        self.register_frame.grid()        
        
        #Set up Help heading (row 0)
        self.register_heading = Label(self.register_frame, text = "Register", 
                                          font = ("Arial", "19", "bold"),
                                          bg = background_colour)
        self.register_heading.grid(row = 0)                
        
        #Registering text (row 1)
        self.text = Label(self.register_frame, text = "Please fill in the details below.", 
                                          font = ("Arial", "10", "bold"),
                                          bg = background_colour)
        self.text.grid(row = 1, column = 1)
        
        #Entering Username (row 2)
        self.username_label = Label(self.register_frame, text = "Username:", 
                              font = ("Arial", "10", "bold"), 
                              bg = background_colour)
        self.username_label.grid(row = 2, column = 0)
        self.new_username = Entry(self.register_frame, width = 20, font = ("Arial", "10", "bold"))
        self.new_username.grid(row = 2, column = 1, padx = 10)
        
        #Entering Password (row 3)
        self.password_label = Label(self.register_frame, text = "Password:", 
                              font = ("Arial", "10", "bold"), 
                              bg = background_colour)
        self.password_label.grid(row = 3, column = 0)
        self.new_password = Entry(self.register_frame, width = 20, font = ("Arial", "10", "bold"))
        self.new_password.grid(row = 3, column = 1, padx = 10)   
        
        #SignUp Button (row 4)
        self.sign_up = Button(self.register_frame, text = "Sign Up", width = 10,
                                     bg = background_colour, font = ("Arial", "10", "bold"),
                                     command = self.register_user)
        self.sign_up.grid(row = 4, pady = 10) 
        
    def register_user(self):
        username_info = self.new_username.get()
        password_info = self.new_password.get()
    
        #file=open("information.txt", "w")
        #file.write("\n")
        #file.write(username_info+",")
        #file.write(password_info)
        #file.close()   
        
        #self.new_username.delete(0, END)
        #self.new_password.delete(0, END)
        
        new_player.append(username_info)
        new_player.append(password_info)
        print(new_player)
        
        root.destroy()
        
        newroot = Tk()
        application = Mainscreen()
        newroot.mainloop()        
 
        
    def close_register(self):
    
        #Put login and register button back to normal...
        self.login_button.config(state = NORMAL)
        self.register_button.config(state = NORMAL)
        self.register_box.destroy()
        
    
    def login(self):
        print("Login session started")
        
        background_colour = "orange"
        
        #Disable login and register buttons
        self.login_button.config(state = DISABLED)
        self.register_button.config(state = DISABLED)
        
        #Sets up child window (i.e. login box)
        self.login_box = Toplevel()
        
        #If user press cross at top, closes login and 'unlocks' the login and register buttons...
        self.login_box.protocol('WM_DELETE_WINDOW', partial(self.close_login))
        
        #Set up GUI Frame
        self.login_frame = Frame(self.login_box, bg = background_colour, pady = 10)
        self.login_frame.grid()        
        
        #Set up Help heading (row 0)
        self.login_heading = Label(self.login_frame, text = "Login", 
                                          font = ("Arial", "19", "bold"),
                                          bg = background_colour)
        self.login_heading.grid(row = 0)      
        
        #Entering Username (row 1)
        self.username_label = Label(self.login_frame, text = "Username:", 
                              font = ("Arial", "10", "bold"), 
                              bg = background_colour)
        self.username_label.grid(row = 1, column = 0)
        self.username_entry = Entry(self.login_frame, width = 20, font = ("Arial", "10", "bold"))
        self.username_entry.grid(row = 1, column = 1, padx = 10)
        
        #Entering Password (row 2)
        self.password_label = Label(self.login_frame, text = "Password:", 
                              font = ("Arial", "10", "bold"), 
                              bg = background_colour)
        self.password_label.grid(row = 2, column = 0)
        self.password_entry = Entry(self.login_frame, width = 20, font = ("Arial", "10", "bold"))
        self.password_entry.grid(row = 2, column = 1, padx = 10)   
        
        #Login Button (row 3)
        self.final_login = Button(self.login_frame, text = "Login", width = 10,
                                     bg = background_colour, font = ("Arial", "10", "bold"),
                                     command = self.login_user)
        self.final_login.grid(row = 3, pady = 10)
        
    def login_user(self):
        #Check username and password entered are correct
        
        for key, value in player_info.items():
            if key == self.username_entry.get() and value == self.password_entry.get():
                
                current_player.append(self.username_entry.get())
                current_player.append(self.password_entry.get())
                print(current_player)                
                
                root.destroy() 
                newroot = Tk()
                application = Mainscreen()
                newroot.mainloop()
                
            else:
                self.error = Label(self.login_frame, text = "Username or password incorrect!",fg = 'Red')
                self.error.grid(row = 4, column = 1)                             
        
        
    def close_login(self):
    
        #Put login and register button back to normal...
        self.login_button.config(state = NORMAL)
        self.register_button.config(state = NORMAL)
        self.login_box.destroy()
        
    
    def __init__(self):
        background_colour = "light blue"
        
        #Frame
        self.startup_screen = Frame(bg = background_colour, pady = 10)
        
        self.startup_screen.grid()        
        
        
        #Heading (row 0)
        self.startup_heading = Label(self.startup_screen, text = "Hangman Game", 
                                          font = ("Arial", "19", "bold"),
                                          bg = background_colour,
                                          padx = 10, pady = 10)
        self.startup_heading.grid(row = 0)
        
        #Login button (row 1)
        self.login_button = Button(self.startup_screen, text = "Login", width = 10,
                                     bg = background_colour, font = ("Arial", "10", "bold"),
                                     command = self.login)
        self.login_button.grid(row = 1, pady = 10) 
        
        #Register button (row 2)
        self.register_button = Button(self.startup_screen, text = "Register", width = 10,
                                     bg = background_colour, font = ("Arial", "10", "bold"),
                                     command = self.register)
        self.register_button.grid(row = 2, pady = 10)          
        

#Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Hangman Game")
    application = Startup()
    
    root.mainloop()