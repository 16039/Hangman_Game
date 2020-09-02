##Starting and Playing Game Screen

##NOT WORKING!

#Importing required functions
import pygame
import math
import random
from tkinter import *

#Lists/Dictionaries
game_images = []
letters = []
words_list = ["AWESOME"]
guessed = []

#Loading in images
for i in range(7):
    each_image = pygame.image.load("hangman" + str(i) + ".png")
    game_images.append(each_image) 

#Colours
pygame_white = (255, 255, 255)
pygame_black =(0, 0, 0)

class PlayGame: 
    
    def __init__(self):
        pygame.init()
        self.game_width = 1000
        self.game_height = 750
        self.game_window = pygame.display.set_mode((self.game_width, self.game_height))
        pygame.display.set_caption("Hangman Game - PlayGame")   
        
        #Fonts
        letter_txt = pygame.font.SysFont('comicsans', 40)
        word_txt = pygame.font.SysFont('comicsans', 60)
        title_txt = pygame.font.SysFont('comicsans', 70)
        
        #Music
        pygame.mixer.music.load("gameplay_music.mp3")
        pygame.mixer.music.play()    
        
        #Button variables
        self.button_radius = 20
        self.button_gap = 15
        self.button_startx = round((self.game_width - (self.button_radius * 2 + self.button_gap) *13)/2)
        self.button_starty = 400
        
        #Importing the letters into the letters list
        A = 65
        for i in range(26):
            self.letter_positionx = self.button_startx + self.button_gap * 2 + ((self.button_radius*2 + self.button_gap) * (i%13))
            self.letter_positiony = self.button_starty + ((i // 13) * (self.button_gap + self.button_radius *2))
            letters.append([self.letter_positionx, self.letter_positiony, chr(A + i), True])
        
        #game variable
        self.gameplay_status = 0
        self.choosen_word = random.choice(words_list) 
        
        self.main()
        
        def draw(self):
            
            #Filling the screen with white colour
            self.game_window.fill(pygame_white)
            
            #Drawing game title
            self.game_title = title_txt.render("HANGMAN", 1, BLACK)
            self.game_window.blit(self.game_title, (self.game_width/2 - self.game_title.get_width()/2, 20)) 
            
            #Game information
            ##Other onscreen text in here
            
            #Drawing word to be guessed
            displaying_word = ""
            for each_letter in chosen_word:
                if each_letter in guessed_letters:
                    displaying_word += each_letter + " "
                else:
                    displaying_word += "_ "
            the_text = word_txt.render(display_word, 1, pygame_black)
            self.game_window.blit(the_text, (400, 200))
            
            #Drawing buttons
            for each_letter in letters:
                self.letter_positionx, self.letter_positiony, self.alphabet_letter, self.visability = each_letter
                if self.visability:
                    pygame.draw.circle(self.game_window, pygame.black, (self.letter_positionx, self.letter_positiony), self.button_radius, 3)
                    the_text = letter_txt.render(each_letter, 1, pygame_black)
                    #Positioning letters to the center
                    self.game_window.blit(the_text, (self.letter_positionx - the_text.get_width()/2, self.letter_positiony - the_text.get_height()/2))
            #Drawing images
            self.game_window.blit(game_images[self.gameplay_status], (150, 100))
            pygame.display.update() 
            
        def displaying_messsages(self, message):

            #Image displayed as game has ended
            pygame.time.delay(1000)
            self.game_window.fill(pygame_white)
            the_text = word_txt.render(message, 1, pygame_black)
            self.game_window.blit(the_text, (self.game_width/2 - the_text.get_width()/2, self.game_height/2 - the_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(3000)        
    
            ##Need to add music

        def main(self):
    
            global gameplay_status
    
            #setup game loop
            FPS = 60
            clock = pygame.time.Clock()
            run = True            
    
            while run:
                clock.tick(FPS)
    
    
                for event in pygame.event.get():
    
                    #When exit button is clicked
                    if event.type == pygame.QUIT:
                        run = False
                        if event.type == pygame.MOUSEBUTTONDOWN:              
                            self.mouse_x, self.mouse_y = pygame.mouse.get_pos() #Mouse position identified
                            for each_letter in letters:
                                self.letter_positionx, self.letter_positiony, self.alphabet_letter, self.visability = each_letter
                                if self.visability:
                                    self.distance = math.sqrt((self.letter_positionx - self.mouse_x)**2 +(self.letter_positiony - self.mouse_y)**2)
                                    if self.distance < self.button_radius:
                                        each_letter[3] = False
                                        guessed.append(self.alphabet_letter)
                                        if self.alphabet_letter not in chosen_word:
                                            self.gameplay_status +=1
    
    
                self.draw()
    
                won = True
                for each_letter in chosen_word:
                    if each_letter not in guessed:
                        won = False
                        break
                if won:
                    self.displaying_messages("You WON! You have gained points!")
                    break
    
                if self.gameplay_status == 6:
                    self.display_message("You LOST! The word was "+word)
                    break

    pygame.quit()
    sys.exit()

if __name__ == __main__:
    PlayGame()