#Papi-Gelato
scoop = 1.10
cones = 1.25
trays = 0.75
scoopQty = 0
conesQty = 0
traysQty = 0

def allTaste(): 
    global tasteLst
    tasteLst = []   
    for x in range(1, iceScoops+1):

        taste = input(f"Welke smaak wilt u voor bolletje nummer {x}?\nA) Aardbei\nC) Chocolade\nM) Munt\nV) Vanille\n").upper()
        if taste == "A":
            tasteLst.append("Aardbei")
        elif taste == "C":
            tasteLst.append("Chocolade")
        elif taste == "M":
            tasteLst.append("Munt")
        elif taste == "V":
            tasteLst.append("Vanille")
        else:
            print("Sorry dat snap ik niet...")
            allTaste()


def step1():
    global iceScoops
    global doosje
    global conesQty
    global traysQty
    global scoopQty
    print("Welkom bij Papi Gelato")
    iceScoops = int(input("Hoeveel bolletjes wilt u?"))
    #if iceScoops != range(8, 50):
        
    if iceScoops < 8:
        allTaste()
        scoopQty += iceScoops
    if iceScoops in range(1, 4):
        step2()
    elif iceScoops in range(4, 8):
        print(f"Dan krijgt u van mij een bakje met {iceScoops} bolletjes met de smaken\n{tasteLst}")
        doosje = 'bakje'
        traysQty += 1
        step3()
    elif iceScoops in range(8, 50):
        print("Sorry, zulke grote bakken hebben we niet")
        step1()
    else:
        print("Sorry dat snap ik niet...")
        step1()

def step2():
    global traysQty
    global conesQty
    global doosje
    x = input(f"Wilt u deze {iceScoops} bolletje(s) in A) een hoorntje of B) een bakje?").upper()
    if x == "A":
        doosje = 'hoorntje'
        conesQty += 1
    elif x == "B":
        doosje = 'bakje' 
        traysQty += 1
    else:
        print("Sorry dat snap ik niet...")
        step2()
    step3()

def step3():
    x = input(f"Hier is uw {doosje} met {iceScoops} bolletje(s) met de smaken\n{tasteLst}.\n Wilt u nog meer bestellen? (Y/N)").upper()
    if x == "Y":
        step1()
    elif x == "N":
        print("Bedankt en tot ziens!")
        receipt()
    else:
        print("Sorry dat snap ik niet...")
        step3()

def receipt():
    print("---------[\"Papi Gelato\"]---------\n")

    print("Bolletjes     {} x €{:.2f}   = €{:.2f}".format(scoopQty, scoop, (scoopQty*scoop)))
    if conesQty != 0:
        print("Horrentjes    {} x €{:.2f}   = €{:.2f}".format(conesQty, cones, (conesQty*cones)))
    if traysQty != 0:
        print("Bakjes        {} x €{:.2f}   = €{:.2f}".format(traysQty, trays, (traysQty*trays)))
    print("                            -------- +")
    print("Totaal                     = €{:.2f}".format((scoopQty*scoop)+(conesQty*cones)+(traysQty*trays)))


step1()