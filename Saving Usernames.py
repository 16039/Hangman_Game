player_info = {}

def appending(): #Definition appends txt information into the program.
    
    reading = open('information.txt', "r") #Txt file is opened.
    line = reading.readlines() #Each line is being read.  

    for i in range(len(line)): #Appending information for player_info dictionary.
        the_line = line[i].split(",")
        the_line[-1] = the_line[-1].strip("\n")

        player_info[the_line[0]] = the_line[1:]

    print(player_info)
      

    reading.close() #Txt file is closed.



appending() #Prompts the program's first definition. 
