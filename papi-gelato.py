#Papi-Gelato

def allTaste(): 
    global tasteLst
    tasteLst = []   
    for x in range(iceScoops):

        taste = input(f"Welke smaak wilt u voor bolletje nummer {iceScoops}?\nA) Aardbei\nC) Chocolade\nM) Munt\nV) Vanille\n").upper()
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
    iceScoops = int(input("Hoeveel bolletjes wilt u?"))
    allTaste()
    if iceScoops in range(1, 4):
        doosje = "hoorntje"
        step2()
    elif iceScoops in range(4, 8):
        print(f"Dan krijgt u van mij een bakje met {iceScoops} bolletjes met de smaken\n{tasteLst}")
        doosje = 'bakje'
        step3()
    elif iceScoops in range(8, 50):
        print("Sorry, zulke grote bakken hebben we niet")
        step1()
    else:
        print("Sorry dat snap ik niet...")
        step1()

def step2():
    global doosje
    x = input(f"Wilt u deze {iceScoops} bolletje(s) in A) een hoorntje of B) een bakje?").upper()
    if x == "A":
        doosje = 'hoorntje'
    elif x == "B":
        doosje = 'bakje' 
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
    else:
        print("Sorry dat snap ik niet...")
        step3()
    
step1()
