import time
totalIceCreamQuan = 0.0
iceCreamQuan = 0
cupQuan = 0
coneQuan = 0
toppingCost = 0.0
toppingQuan = 0
chosenContainer = ""
flavour = ""
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def howManyBalls(): #The part where it asks how manny balls of icecream you want
    global iceCreamQuan
    time.sleep(0.5)

    #Asks the user how much balls of icecream they want
    print()
    print("----------Bolletjes----------")
    iceCreamQuan = str(input("Hoeveel bolletjes wilt u? >>"))

    #If the input contains letters
    for i in range(len(iceCreamQuan)):
        if iceCreamQuan[i] in alphabet: print("Voer geen letters in alstublieft, alleen getallen"); howManyBalls()
    
    #If the user enters a decimal number
    if float(iceCreamQuan) % 1 != 0: print("Helaas, wij serveren alleen hele bolletjes, voer een heel getal in"); howManyBalls()
    else: iceCreamQuan = int(iceCreamQuan)

    #If the user enters zero
    if iceCreamQuan <= 0:print("Je moet ten minste 1 bolletje kiezen"); howManyBalls()

    #If the user enters a different number
    elif iceCreamQuan >= 1 and iceCreamQuan <= 3:
        chooseFlavour()
    elif iceCreamQuan > 3 and iceCreamQuan < 8:
        print(f"Dan krijgt u van mij een bakje met {iceCreamQuan} bolletjes");time.sleep(1); chooseFlavour()
    elif iceCreamQuan >= 8 : 
        print("Sorry, maar zulke grote bakken hebben we niet"); howManyBalls()

    #If the user enters anything else
    else:
        print("Sorry, dat snap ik niet..."); howManyBalls()


def chooseFlavour():
    global flavour
    global iceCreamQuan
    global cupQuan
    global chosenContainer
    print()
    print("------------smaak------------")
    print("U heeft keuze uit 4 smaken:")
    time.sleep(0.1)
    print("A) Aardbei")
    time.sleep(0.1)
    print("C) Chocolade")
    time.sleep(0.1)
    print("M) Munt")
    time.sleep(0.1)
    print("V) Vanille")
    for i in range(iceCreamQuan):
        def ask(i): #Made this just so you dont have to repeat the entire number of balls again if you mess one up
            global flavour
            print(f"Welke smaak wilt u voor bolletje {i + 1}?")
            flavour = input(">>")

            #If the user doenst choose one, repeat in the same iteration
            if flavour.lower() != "a" and flavour.lower() != "c" and flavour != "m" and flavour != "v":
                print("Dat snap ik niet...") 
                time.sleep(0.5)
                print("Kies alstublieft A, C, M of V")
                ask(i)
        ask(i)

    #Chooses whether to send the user right to the checkout or let them choose their container based on the quantity of balls
    if iceCreamQuan >= 1 and iceCreamQuan <= 3:
        coneOrCup()
    elif iceCreamQuan > 3 and iceCreamQuan < 8:
        cupQuan += 1
        chosenContainer = "bakje"
        print(f"Hier is uw bakje met {iceCreamQuan} bolletjes")
        chooseTopping()


def coneOrCup(): #Asks if the user wants a cone or cup
    global iceCreamQuan 
    global cupQuan
    global coneQuan
    global chosenContainer
    print()
    print("-------Hoorntje of bakje-------")
    time.sleep(0.5)
    print(f"Wilt u deze {iceCreamQuan} bolletjes in:")
    time.sleep(0.1)
    print("A) een hoorntje")
    time.sleep(0.1)
    print("B) een bakje")
    
    chosenContainer = input(">>")
    if chosenContainer.lower() == "a": 
        chosenContainer = "hoorntje"
        coneQuan +=1
        print(f"Hier is uw {chosenContainer} met {iceCreamQuan} bolletjes")
        chooseTopping()
    elif chosenContainer.lower() == "b":
        cupQuan +=1 
        chosenContainer = "bakje"
        print(f"Hier is uw {chosenContainer} met {iceCreamQuan} bolletjes")
        chooseTopping()
    else: 
        print("Dat snap ik niet...")
        time.sleep(0.5)
        print("Kies alstublieft A of B")
        coneOrCup()


def chooseTopping(): #Lets the user pick a topping
    global toppingCost
    global toppingQuan
    global iceCreamQuan
    global chosenContainer
    print("")
    print("-----------topping-----------")
    print("Wilt u er nog een topping op?")
    time.sleep(0.1)
    print("A) Geen")
    time.sleep(0.1)
    print("B) Slagroom")
    time.sleep(0.1)
    print("C) Sprinkels")
    time.sleep(0.1)
    print("D) Caramel saus")
    topping = input(">>")
    #Calculates the topping cost based of the decision, quantity of balls and the container
    if topping.lower() == "a": repeatOrStop()   
    else: toppingQuan += 1
    if topping.lower() == "b": toppingCost += 0.5; repeatOrStop()
    elif topping.lower() == "c": toppingCost += iceCreamQuan * 0.3; repeatOrStop()
    elif topping.lower() == "d":
        if chosenContainer == "hoorntje": toppingCost += 0.6; repeatOrStop()
        elif chosenContainer == "bakje": toppingCost += 0.9; repeatOrStop()

def repeatOrStop(): #Asks if the user is done or want to order again
    global totalIceCreamQuan
    global iceCreamQuan
    global coneQuan
    global cupQuan
    global toppingCost
    global toppingQuan
    time.sleep(0.5)
    print()
    repeatORder = input("Wilt u nogmeer bestellen? Y/N >>")
    if repeatORder.lower() == "y": totalIceCreamQuan += iceCreamQuan;howManyBalls()

    elif repeatORder.lower() == "n":#Shows the receipt
        totalIceCreamQuan += iceCreamQuan
        print()
        print()
        print()
        print()
        print()
        print("---------['Papi Gelato']---------")
        print(f"Bolletjes     {totalIceCreamQuan} x €1.10  = €{totalIceCreamQuan * 1.10}")
        if coneQuan > 0:
            print(f"Hoorntje      {coneQuan} x €1.25    = €{float(coneQuan * 1.25)}")
        if cupQuan > 0:
            print(f"Bakje         {cupQuan} x €0.75    = €{float(cupQuan * 1.25)}")
        if toppingQuan > 0:
            print(f"topping       1 x €{toppingCost}     = €{toppingCost}")
        print("                         --------- +")
        print(f"Totaal                     = €{float(totalIceCreamQuan * 1.10 + coneQuan * 1.25 + cupQuan * 1.25 + toppingCost)}")

        print("Bedankt en tot ziens!")

    else: print("Dat snap ik niet..."); time.sleep(1); print("Kies alstublieft Y of N"); repeatOrStop()


#The user starts here
print("Welkom bij Papi Gelato!.")
time.sleep(1)

howManyBalls()
input()