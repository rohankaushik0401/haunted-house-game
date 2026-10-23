

import random
print("Welcome to srks haunted house ")
print("Enter pin to leave ")
print("You'll find the pin scattered or together in any of the 4 rooms")
print("But beware , there are monsters in the house nd it attacks you for every mistake \n be sure to go to every room and find every clue")
pocket=[]
drawer=["pistol"]
cupboard=["bigKey"]
computertable=["Smallkey"]
fridge=["waterbottle"]
carkey=random.randint(1,2)
life=random.randint(90,110)
pin1=random.randint(0,9)
pin2=2
pin3=random.randint(0,9)
ch1=["srkshaunted","srks haunted"]


    
def monster():
    global life
    
    damage=random.randint(5,20)
    damage2=random.randint(20,30)
    
    if "pistol" in pocket:
        
        gun=int(input("there is a monster\nTo use gun \n guess a random number bw 0 to 3 to shoot "))
        attack=random.randint(0,4)
        
        if gun==attack:
            print("success,Monster is wounded, no life lost")
        else:
            life-=damage
            if (life<0):
                life=0
            print("Shot missed now ,monster has attacked you",damage,"life lost",life,"life reamaining")
    else:     
        life-=damage2
        if (life<0):
                life=0
        print("monster has attacked you ",damage2,"life lost",life,"life reamaining")

        
def bigmonster():
    global life
    damage=random.randint(15,20)
    damage2=random.randint(30,40)
    damage3=random.randint(0,5)
    
    if "pistol" in pocket:
        
        gun=int(input(" there is a monster\nto use gun\nGuess a random number bw 0 to 3 to shoot "))
        attack=random.randint(0,3)
        if gun==attack:
            life-=damage3
            if (life<0):
                life=0
            print(" big monster wounded",damage3,"only life lost",life,"life reamining")
        else:
            life-=damage
            if (life<0):
                life=0
            print("shot missed , big monster has attacked ",damage,"life lost",life,"life reamaining")
    else:      
        life-=damage2
        if (life<0):
                life=0
        print("big monster has attacked ",damage2,"life lost",life,"life reamaining")
            

    
def bedroom():
    choice=0
    while choice!=4:
             choice=eval(input("\nEnter 1 to search bed \n      2 To search table drawer \n      3 To search cupboard \n      4 To leave room \nEnter: "))
            
             if choice==1:
                print("What\'s that?? There is a letter, Do you wish to read? \n ")
                ch=input("Yes or No: ").lower()
                if ch=="yes":
                    print ("OOPS!! \nThe letter is cursed ")
                    monster()
                    print("The pin to leave is kept secretly \nYou'll find the 3 clues in other 3 rooms but before you leave, there are some useful equipment in this room")                     
             elif choice==2:
                print ("Click \'o\' to open Drawer")
                ch=input().lower()
                if ch=="o":
                    if len(drawer)!=0 and len(pocket) in range(1,2):
                        for i in drawer:
                            print("There is",i)
                            print("Click \'u\' to Equip\nClick \'r\' to Replace\nAny other to exit\nEnter: ")
                            ch2=input().lower()
                            if ch2=="r":
                                print("Test retard")
                                x=pocket.pop()
                                pocket.insert(0,i)
                                print("You have", pocket,"in your pocket")
                                drawer.pop()
                                drawer.append(x)
                            elif ch2=="u":
                                print("Test")
                                drawer.pop()
                                pocket.insert(0,i)
                                print("You have", pocket,"in your pocket")
                            else:
                                break
                                
                                    
                    elif len(pocket)==0 and len(drawer)!=0:
                         for i in drawer:
                            print("OHHH, There is ",i)
                            print("Click \'u\' to equip")
                            ch2=input().lower()
                            if ch2=="u": 
                                pocket.insert(0,i)
                                drawer.pop()
                                print("You have", pocket,"in your pocket")

                            else:
                                break
                            
                    elif len(pocket)==2 and len(drawer)!=0:
                        for i in drawer:
                                print("There is ",i)
                                print("Click \'r\' to replce")
                                ch2=input().lower()
                                if ch2=="r":
                                    x=pocket.pop()
                                    pocket.insert(0,i)
                                    print("You have", pocket,"in your pocket")
                                    drawer.pop()
                                    drawer.append(x)
                                else:
                                    break
                            
                        
                    else:
                        print("Nothing to equip")
             elif choice==3:
                print ("Click \'o\' to open cupboard")
                ch=input()
                if ch=="o"or"O":
                    if len(cupboard)!=0 and len(pocket) in range(1,2):
                        for i in cupboard:
                            print("There is ",i)
                            print("Click \'u\' to equip"
                                  "\n\'r\' to replace "
                                  "\nAny other to exit\nEnter: ")
                            ch2=input().lower()
                            if ch2=="r":
                                x=pocket.pop()
                                pocket.insert(0,i)
                                print("You have", pocket,"in your pocket")
                                cupboard.pop()
                                cupboard.append(x)
                            elif ch2=="u":
                                cupboard.pop()
                                pocket.insert(0,i)
                                print("You have", pocket,"in your pocket")
                            else:
                                break
                    elif len(pocket)==0 and len(cupboard)!=0:
                         for i in cupboard:
                            print("There is ",i)
                            print("Click \'u\' to equip")
                            ch2=input()
                            if ch2=="u"or"U":
                             pocket.insert(0,i)
                             cupboard.pop()
                             print("You have", pocket,"in your pocket")
                            else:
                                break
                                
                    elif len(pocket)==2 and len(cupboard)!=0:
                             for i in cupboard:
                                print("There is ",i)
                                print("Click \'r\' to replce")
                                ch2=input()
                                if ch2=="r":
                                    x=pocket.pop()
                                    pocket.insert(0,i)
                                    print("You have", pocket,"in your pocket")
                                    cupboard.pop()
                                    cupboard.append(x)
                                else:
                                    break
                    else:
                        print("Nothing to equip")
                else:
                    break
             elif choice==4:
                print("You left the room, \nohhh !! There is the MONSTER behind the door")
                monster()
             else:
                 print("Wrong choice ")
                 monster()
    
def livingroom():
    global pin3
    choice=0
    while choice!=3:
        choice=int(input("Enter 1 to search sofaa\n      2 to search computer table,      3 to leave\nEnter: "))
        if choice==1:
            print("There is newspaper")
            print("Press x to read")
            ch=input().lower()
            if ch=="x":
                print("Article 1: The monster cannot be killed")
                print("Article 2: One of digits of pin number is ", pin3)
                print("Article 3: The monster cannot attack in the living room")
            else:
                break
        elif choice==2:
            print ("Click o to search")
            ch=input().lower()
            if ch=="o":
                if len(computertable)!=0 and len(pocket) in range(1,2):
                    for i in computertable:
                        print("There is ",i)
                        print("Click u to equip"
                              "\n     r to replace "
                              "\n     Any other to exit\nEnter: ")
                        ch2=input().lower()
                        if ch2=="r":
                            x=pocket.pop()
                            pocket.insert(0,i)
                            print("You have", pocket,"in your pocket")
                            computertable.pop()
                            computertable.append(x)
                        elif ch2=="u":
                            computertable.pop()
                            pocket.insert(0,i)
                            print("You have", pocket,"in your pocket")
                        else:
                            break    
                elif len(pocket)==0 and len(computertable)!=0:
                     for i in computertable:
                        print("There is ",i)
                        print("Click u to equip")
                        ch2=input()
                        if ch2=="u".lower():
                         pocket.insert(0,i)
                         computertable.pop()
                         print("You have", pocket,"in your pocket")
                        else:
                            break
                elif len(pocket)==2 and len(computertable)!=0:
                        for i in computertable:
                            print("There is ",i)
                            print("Click r to replce")
                            ch2=input().lower()
                            if ch2=="r":
                                x=pocket.pop()
                                pocket.insert(0,i)
                                print("You have", pocket,"in your pocket")
                                computertable.pop()
                                computertable.append(x)
                            else:
                                break
                else:
                    print("Nothing to equip")
            else:
                break
        elif choice==3:
            print("You left the room")
        else:
            print("Wrong choice, Try again")
            print("Since you're in living room ,You\'re safe for now")
            
def diningroom():
    global pin2
    choice=0
    while choice!=3:
        choice=int(input("Click 1 to search dining table\n      2 to search fridge\n      3 to leave\nEnter: "))
        if choice==1:
                   print("Do you want the number directly? Beware of consequences")
                   ch=input("Yes/No? ").lower()
                   if ch=="yes":
                      monster()
                      print(pin2 ,"is a digit of pin")
                   else:
                       print("Wise choice")
                       print("The number is the number of monsters in this game")
        elif choice==2:
            print ("Click o to search")
            ch=input().lower()
            if ch=="o":
                if len(fridge)!=0 and len(pocket) in range(1,2):
                    for i in fridge:
                        print("There is ",i)
                        print("Click u to equip\n      r to replace\n     Any other to exit\nEnter: ")
                        ch2=input().lower()
                        if ch2=="r":
                            x=pocket.pop()
                            pocket.insert(0,i)
                            print("You have", pocket,"in your pocket")
                            fridge.pop()
                            fridge.append(x)
                        elif ch2=="u":
                            fridge.pop()
                            pocket.insert(0,i)
                            print("You have", pocket,"in your pocket")
                        else:
                            break    
                elif len(pocket)==0 and len(computertable)!=0:
                     for i in fridge:
                        print("There is ",i)
                        print("Click u to equip\nEnter: ")
                        ch2=input().lower()
                        if ch2=="u":
                             pocket.insert(0,i)
                             fridge.pop()
                             print("You have", pocket,"in your pocket")                        
                        else:
                            break
                elif len(pocket)==2 and len(fridge)!=0:
                        for i in fridge:
                            print("There is ",i)
                            print("Click r to replace\nEnter: ")
                            ch2=input().lower()
                            if ch2=="r":
                                x=pocket.pop()
                                pocket.insert(0,i)
                                print("You have", pocket,"in your pocket")
                                fridge.pop()
                                fridge.append(x)
                            else:
                                break
                else:
                    print("Not available currently to equip")
            else:
                break
        elif choice==3:
            print("You left the room")
        else:
            print("Wrong choice")
            monster()
            
def kitchen():
    global pin1
    xx=1
    choice=9
    while choice!=4:
        choice=int(input("press 1 to inspect gas\n     2 to inspect sink\n     3 to inspect shelves\n     4 to leave"))
        if choice==1:
            if xx==1 and "waterbottle" not in pocket:
                 print ("The gas is on fire, This summons the big monster ")
                 print("You made a huge mistake not carrying the water bottle, don\'t repeat this near gas")
                 bigmonster()
                 xx+=1
            else:
                print("There is another big monster which is summoned by fire")
        elif choice==2:
            if xx==1:
                print("The monster has heard you, shout the name of this house to escape")
                ch=input().lower()
                if ch in ch1:
                    print("You ESCAPE")
                else:
                    monster()
                xx+=1
            print("The pin found in living room is the 3rd digit")
            print("The pin in dining room is second digit")
            print("The pin in kitchen is the 1st digit")
        elif choice==3:
            print("There is a die\nRoll it for the pin reveal")
            print("click q to roll\nEnter: ")
            ch2=input().lower()
            if ch2=="q":
                print("and the die rollS",pin1)
            else:
                break
        elif choice==4:
            print("You left")
        else:
            print("Wrong move")
            monster()

def pindoor():
    global game
    global carkey
    global life
    pin=input("Enter pin: ")
    if pin==str(pin1)+str(pin2)+str(pin3):
        if carkey==1:
            print("You escape the house ")
            print("But the monster has heard you")
            print("There is a car ,quick....\nUse the smallkey to drive")
            choice=int(input("Enter 1 to re-enter the house\n      2 to approach car\nEnter: "))
            if choice==1:
                monster()
            else:
                if "Smallkey" in pocket:
                     print
                     print("Click p to open car\nEnter: ")
                     ch=input()
                     if ch=="p":
                        print("YOUUU WON")
                        life=0
                     else:
                         monster()
                else:
                    monster()
    
                       
            
        elif carkey==2:
            print("You escape the house")
            print("But the monster has heard you")
            print("There is a car quick...\nUse the BIGKEY to drive")
            choice=int(input("Enter 1 to re-enter the house,      2 to approach car\nEnter: "))
            if choice==1:
                monster()
            else:
                if "bigKey" in pocket:
                    print("Click p to open car\nEnter: ")
                    ch=input().lower()
                    if ch=="p":
                        print("YOU WON ")
                        life=0
                    else:
                        monster()
                else:
                    monster()
    else:
        print("Wrong Pin")
        monster()
#gameplay
while life>0:
    print("you have ",life,"life")
    choice1=input("Enter 1 to enter bedroom \n      2 To enter livingroom \n      3 To enter dining room \n      4 To enter kitchen \n      5 To approach exit door \n Your input: ")

        
    if choice1=="1":
        bedroom()
    elif choice1=="2":
        livingroom()
    elif choice1=="3":
        diningroom()
    elif choice1=="4":
        kitchen()
    elif choice1=="5":
        pindoor()
    else:
        print("wrong move")
        bigmonster()
else:
    print("game over ")
                
                
                
        
            

        
        
            
        
        
            
         
            
                
            
                
                    
                
                
                
                
        
                       
                  
