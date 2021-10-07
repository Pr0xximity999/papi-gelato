import time
from typing import Counter
succeed = False
iceCreamQuan = 0
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def howManyBalls(): #The part where it asks how manny balls of icecream you want
    time.sleep(1)

    #Asks the user how much balls of icecream they want
    iceCreamQuan = str(input("Hoeveel bolletjes wilt u? >>"))

    #If the input contains letters
    for i in range(len(iceCreamQuan)):
        if iceCreamQuan[i] in alphabet: print("Voer geen letters in alstublieft"); howManyBalls()
    
    #If the user enters a decimal number
    if float(iceCreamQuan) % 1 != 0: print("Helaas, wij serveren alleen hele bolletjes"); howManyBalls()
    else: iceCreamQuan = int(iceCreamQuan)

    #If the user enters zero
    if iceCreamQuan <= 0:print("Je mag niet minder dan 1 bolletje kiezen"); howManyBalls()

    #If the user enters a different number
    elif iceCreamQuan >= 1 and iceCreamQuan <= 3:
        coneOrCup(iceCreamQuan)
    elif iceCreamQuan > 3 and iceCreamQuan < 8:
        print(f"Dan krijgt u van mij een bakje met {iceCreamQuan} bolletjes"); repeatOrStop()
    elif iceCreamQuan >= 8 : 
        print("Sorry, maar zuk grote bakken hebben we niet"); howManyBalls()

    #If the user enters anything else
    else:
        print("Sorry, dat snap ik niet..."); howManyBalls()



def coneOrCup(iceCreamQuan): #Asks if the user wants a cone or cup
    time.sleep(1)
    print(f"Wilt u deze {iceCreamQuan} bolletjes in:")
    time.sleep(0.5)
    print("A) een hoorntje")
    time.sleep(0.5)
    print("B) een bakje")
    chosenContainer = input(">>")
    if chosenContainer.lower() == "a": 
        chosenContainer = "hoorntje"
        print(f"Hier is uw {chosenContainer} met {iceCreamQuan} bolletjes")
        repeatOrStop()
    elif chosenContainer.lower() == "b": 
        chosenContainer = "bakje"
        print(f"Hier is uw {chosenContainer} met {iceCreamQuan} bolletjes")
        repeatOrStop()
    else: 
        print("Dat snap ik niet...")
        time.sleep(1)
        print("Kies alstublieft A of B")
        coneOrCup()

def repeatOrStop(): #Asks if the user is done or want to order again
    time.sleep(1)
    repeatORder = input("Wilt u nogmeer bestellen? Y/N >>")
    if repeatORder.lower() == "y": howManyBalls()
    elif repeatORder.lower() == "n": print("Bedankt en tot ziens!")
    else: print("Dat snap ik niet..."); time.sleep(1); print("Kies alstublieft Y of N"); repeatORder


print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")
time.sleep(2)

howManyBalls()
input()


