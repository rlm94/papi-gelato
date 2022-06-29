#Papi-Gelato

order = True
scoop = 0.95
cones = 1.25
trays = 0.75
cream = 0.50
sprinkles = 0.30
caramel = 0.60
ice_liter = 9.80
ice_literQty = 0
iceQty = 0
scoopQty = 0
conesQty = 0
traysQty = 0
creamQty = 0
sprinklesQty = 0
caramelQty = 0
toppingsQty = 0
toppingsCounter = 0


def welcome():
    print("Welkom bij Papi Gelato")

def sorry():
    print("Sorry dat is geen optie die we aanbieden...")

def iceScoops():
    global scoopQty, scoops
    scoops = int(input("Hoeveel bolletjes wilt u?"))
    scoopQty += scoops
    return scoops


def tray_or_cone():
    global trayOrCone, conesQty, traysQty, caramel
    trayOrCone = input(f"Wilt u deze {scoops} bolletje(s) in A) een hoorntje of B) een bakje?").upper()
    if trayOrCone == "A":
        trayOrCone = "hoorntje"
        conesQty += 1
    elif trayOrCone == "B":
        trayOrCone = "bakje"
        traysQty += 1    
    return trayOrCone



def allTaste(type,qty):
    global tasteLst
    global client

    tasteLst = []


    for i in range(1,qty+1):
        taste = input(f"Welke smaak wilt u voor {type} nummer {i}?\nA) Aardbei\nC) Chocolade\nV) Vanille\n").upper()#
        if taste == "A":
            tasteLst.append("Aardbei")
        elif taste == "C":
            tasteLst.append("Chocolade")
        elif taste == "V":
            tasteLst.append("Vanille")
        else:
            sorry()
    return tasteLst


def receipt():

    print("---------[\"Papi Gelato\"]---------\n")
    if scoopQty != 0:
        print("Bolletjes     {} x €{:.2f}   = €{:.2f}".format(scoopQty, scoop, (scoopQty*scoop)))
    if conesQty != 0:
        print("Horrentjes    {} x €{:.2f}   = €{:.2f}".format(conesQty, cones, (conesQty*cones)))
    if traysQty != 0:
        print("Bakjes        {} x €{:.2f}   = €{:.2f}".format(traysQty, trays, (traysQty*trays)))
    if toppingsQty != 0:
        print("Toppings      {} x €{:.2f}   = €{:.2f}".format(toppingsCounter, toppingsQty, (toppingsQty)))
    if ice_literQty != 0:
        print("Liter         {} x €{:.2f}   = €{:.2f}".format(ice_literQty, ice_liter, (ice_liter*ice_literQty)))
    print("                            -------- +")
    print("Totaal                    = €{:.2f}".format((scoopQty*scoop)+(conesQty*cones)+(traysQty*trays)+(toppingsQty)+(ice_liter*ice_literQty)))
    if ice_literQty != 0:
        print("BTW(6%)                   = €{:.2f}".format((ice_liter*ice_literQty/106*6)))
def toppings():
    global toppingsQty
    global toppingsCounter
    global caramel
    global trayOrCone
    toppingsInput = input("\n A) Geen\n B) Slagroom\n C) Sprinkels\n D) Caramel Saus\nWat voor topping wilt u:").upper()
    if toppingsInput == "A":
        print("Oke u gaat voor geen toppings.")
    elif toppingsInput == "B":
        toppingsQty += cream
        toppingsCounter += 1       
    elif toppingsInput == "C":
        toppingsQty += sprinkles
        toppingsCounter += 1
    elif toppingsInput == "D":
        toppingsQty += caramel
        toppingsCounter += 1
        if trayOrCone == "bakje":
            toppingsQty += 0.30
    else:
        sorry()

def typeClient():
    global client
    client = input("Bent u A) particulier of B) zakelijk?\n:").upper()
    if client == "A":
        client = "particulier"
    elif client == "B":
        client = "zakelijk"
    else:
        sorry()
    return client
        

while order == True:
    welcome()
    typeClient()
    if client == "particulier":
        type = "bolletje"
        iceScoops()

        if scoops in range(1, 4):
            tray_or_cone()
            toppings()
            allTaste(type, scoops)
            stop_or_go = input(f"Hier is uw {trayOrCone} met {scoops} bolletje(s) met de smaken\n{tasteLst}.\n Wilt u nog meer bestellen? (Y/N)").upper()#
            if stop_or_go == "Y":
                order = True
            elif stop_or_go == "N":
                receipt()
                print("Bedankt en tot ziens!")
                order = False

        elif scoops in range(4, 8):
            traysQty += 1
            trayOrCone = "bakje"
            toppings()
            allTaste(type, scoops)
            print(f"Dan krijgt u van mij een bakje met {scoops} bolletjes met de smaken\n{tasteLst}  ")#
            stop_or_go = input("Wilt u nog meer bestellen? (Y/N)\n:").upper()
            if stop_or_go == "Y":
                order = True
            elif stop_or_go == "N":
                receipt()
                print("Bedankt en tot ziens!")
                order = False

        elif scoops in range(8, 50):
            print("Sorry, zulke grote bakken hebben we niet")
        else:
            sorry()
    elif client == "zakelijk":
        type = "liter"
        businessInput = int(input("Hoeveel liter ijs wilt u?"))
        ice_literQty += businessInput
        allTaste(type, businessInput)
        receipt()
        order = False
    else:
        sorry()
