import random
while True:
    
    a=["r","p","s"]

    player_computer= random.choice(a)
    print(player_computer)
    player1=input("Plis write R for rock, P for paper, or S for scissors ")


    if player1.lower()== player_computer:
        print("bez sera")
        continue
            
    elif player1.lower()=="r" and player_computer=="s":
        print("congrats U won Rock bited Sicors")
        break
            
    elif player1.lower()=="p" and player_computer=="r":
        print("congrats U won Paper bited Rosk")
        break
        
            
    elif player1.lower()=="s" and player_computer=="p":
        print("congrats U won Sicors bited paper")
        break
    else:
        print("Sadeg u lost")
        break
