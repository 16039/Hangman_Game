##Appending and Recieving

##NEED TO LOOK AT ASSESSMENT DATABASE CODE

#Dictionaries and lists
player_info = {'Mr':['Dad',6], 'Mrs':['Mum', 4], 'Little':['Bird', 2]}
appending_player = []
current_player = []
current_score = []

for key, value in player_info.items():
    print("Username: ", key)
    print("Password: ", value[0])
    print("Score: ", value[1])

user = input("Name? ")
pas = input("Pass? ")
score = 0

appending_player.append(pas)
appending_player.append(score)

for key,value in player_info.items():
    if score < value[1]:
        index = value[1].index()
        print(index)
        




for key, value in player_info.items():
    print("Username: ", key)
    print("Password: ", value[0])
    print("Score: ", value[1])
