##Sorting Highscores

#highscore_list = {'DVA':['NERFTHIS', '7'], 'ASHE':['BOB', '5'], 'WINSTON':['BANANAS', '3'], 'MERCY':['GENJI', '2']}

#highscore_list.sort(key=lambda e: e[1], reverse=True)
#listBox.insert(END, "Position | Name      \t\t |Score\n")
#listBox.insert(END,"-----------------------------------")
#listBox.insert(END,"\n")    


from tkinter import *

def show():

    #tempList= [['Jim', '0.33'], ['Dave', '0.67'], ['James', '0.67'], ['Eden', '0.5']]
    tempList= [['DVA', 'NERFTHIS', '3'], ['ASHE', 'BOB', '5'], ['WINSTON', 'BANANAS', '3'], ['MERCY', 'GENJI', '2']]

    tempList.sort(key=lambda e: e[2], reverse=True)
    listBox.insert(END, "Position | Name      \t\t |Score\n")
    listBox.insert(END,"-----------------------------------")
    listBox.insert(END,"\n")

    for i in range(len(tempList)):
        listBox.insert(END,(i+1))
        listBox.insert(END,"\t |")
        listBox.insert(END,tempList[i][0])
        listBox.insert(END,"\t \t|")
        listBox.insert(END,tempList[i][2])
        listBox.insert(END,"\n")

scores = Tk() 
label = Label(scores, text="High Scores", font = ("Arial",30)).grid(row = 0, columnspan = 3)
listBox= Text(scores,width = 40)
listBox.grid(row = 1,column= 0, columnspan = 2)
showScores = Button(scores, text = "Show scores",width = 15, command = show).grid(row = 4, column = 0)
closeButton = Button(scores, text = "Close",width = 15, command = exit).grid(row = 4, column = 1)

scores.mainloop()