from tkinter import *
from functools import partial
from string import ascii_uppercase
import random

word_list = ["CAT", "DOG", "MELON", "QWERTY"]

class Game:
    
    def guess(self, letter):
        global numberOfGuesses
        if numberOfGuesses <11:
            txt = list(the_word_withSpaces)
            guessed = list(lblWord.get())
            if the_word_withSpaces.count(letter)>0:
                for c in range(len(txt)):
                    if txt[c] == letter:
                        guessed[c] = letter
                    lblWord.set("".join(guessed))
                    if lblWord.get() == the_word_withSpaces:
                        messagebox.showinfo("Hangman", "You guessed it!")
            else:
                numberOfGuesses+=1
                self.imgLabel.config(image = photos[numberOfGuesses])
                if lblWord.get() == the_word_withSpaces:
                    messagebox.showinfo("Hangman", "Game over!")
    
    def startGame(self):
        global the_word_withSpaces
        global numberOfGuesses
        
        numberOfGuesses = 0
        self.imgLabel.config(image = photos[0])
        the_word = random.choice(word_list)
        
        the_word_withSpaces = " ".join(the_word)
        lblWord.set(" ".join("_"*len(the_word)))
        
    
    def __init__(self):
        
        background_colour = "pink"
        
        #Frame
        self.game_screen = Frame(bg = background_colour, pady = 10)
        self.game_screen.grid() 
        
        global photos
        photos = [PhotoImage(file ="image1.png"), PhotoImage(file ="image2.png"), PhotoImage(file ="image3.png"), 
                  PhotoImage(file ="image4.png"), PhotoImage(file ="image5.png")]
        
        self.imgLabel = Label(self.game_screen)
        self.imgLabel.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 10)
        self.imgLabel.config(image = photos[0])
        
        global lblWord
        lblWord = StringVar()
        
        self.something = Label(self.game_screen, textvariable = lblWord, font = ("Arial", "24", "bold"))
        self.something.grid(row = 0, column = 3, columnspan = 6, padx = 10)
        
        
        n=0
        for c in ascii_uppercase:
            self.the_buttons = Button(self.game_screen, text=c, command=lambda c=c: self.guess(c), font = ("Arial", "10"), width = 4)   
            self.the_buttons.grid(row = 1+n//9, column = n%9)
            n+=1
        
        self.startGame()
        
        


#Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Hangman Game")
    application = Game()
    
    root.mainloop()