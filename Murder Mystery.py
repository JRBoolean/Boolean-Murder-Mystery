
import time
import random



flashlight = 0
magnifying = 0
dna = 0
book = 0
evidence = 0

def Roll(t, e):
    x = random.randint(0, 10)
    while e>1:
        x+=e
    print(x)
    if x>4:
        print("You have found evidence")
        e += 1
    else:
        if t>0:
            print("Would you like to use a tool? You have: ",t)
            ans99 = input("Y or N: ")
            if ans99 == "Y":
                x+=4
                t-=1
            Roll(t, e)
    print(t, e)            
    return t, e


print ("Welcome to:")
time.sleep(1)
print("Generic Murder Mystery Name")

print("murder mystery setup")

print("Which tool would you like to take A: The flashlight B: magnifying Glass C: dna test D: How to talk to people book")

for i in range (3):
    ans2 = input("Which item would you like to take?: ")
    time.sleep(0)
    if ans2 == "A":
        print("You have taken the flashlight")
        flashlight +=1


    elif ans2 == "B":
        print("You have taken the magnifying Glass")
        magnifying += 1

    elif ans2 == "C":
        print("You have taken the dna test")
        dna += 1

    elif ans2 == "D":
        print("You have taken the book")
        book += 1
    
    


print("You have taken:")
print(flashlight, "flashlight(s)")
print(magnifying, "magnifying Glasses")
print(dna, "dna Test(s)")
print(book, "book(s)")
time.sleep(0.1)
print("You may enter three different rooms. 1: The Living Room 2: The Bathroom 3: The Dining Room")

ans1 = input("Where would you like to enter?: ")

if ans1 == "1":
    print("You have entered the Living Room")
    ans3 = input("Where would you like to investigate A: The couch B: The closet C: The Butler: ")

    if ans3 == "A":
        print("You have chosen to investigate the couch. You will now roll to see how well you investigate")
        magnifying, evidence = Roll(magnifying, evidence)
    elif ans3 == "B":
        print("You have chosen to investigate the closet. You will now roll to see how well you investigate")
        flashlight, evidence = Roll(flashlight, evidence)
    if ans3 == "C":
        print("You have chosen to investigate the Butler. You will now roll to see how well you investigate")
        book, evidence = Roll(book, evidence)
    time.sleep(1)
    print("You may enter three different rooms. 1: The Garden 2: The Roof 3: The Pool")
    ans12 = input("Where would you like to enter?: ")

elif ans1 == "2":
    print("You have entered the Bathroom")
    ans5 = input("Where would you like to investigate A: The sink B: The toilette C: The window: ")

    if ans5 == "A":
            print("You have chosen to investigate the sink. You will now roll to see how well you investigate")
            flashlight, evidence =Roll(flashlight, evidence)
    elif ans5 == "B":
            print("You have chosen to investigate the toilette. You will now roll to see how well you investigate")
            magnifying, evidence =Roll(magnifying, evidence)
    if ans5 == "C":
            print("You have chosen to investigate the Window. You will now roll to see how well you investigate")
            dna, evidence =Roll(dna, evidence)
    time.sleep(1)
    print("You may enter three different rooms. 1: The Garden 2: The Roof 3: The Pool")
    ans12 = input("Where would you like to enter?: ")

elif ans1 == "3":
    print("You have entered the Dining Room")
    ans9 = input("Where would you like to investigate A: Dining Table B: The Cabinet C: The Cook: ")

    if ans9 == "A":
            print("You have chosen to investigate the Table. You will now roll to see how well you investigate")
            dna, evidence =Roll(dna, evidence)
    elif ans9 == "B":
            print("You have chosen to investigate the Cabinet. You will now roll to see how well you investigate")
            flashlight, evidence =Roll(flashlight, evidence)
    elif ans9 == "C":
            print("You have chosen to investigate the Cook. You will now roll to see how well you investigate")
            book, evidence =Roll(book, evidence)
    time.sleep(1)
    print("You may enter three different rooms. 1: The Garden 2: The Roof 3: The Pool")
    ans12 = input("Where would you like to enter?: ")


if ans12 == "1":
     print("You have entered the Garden")
     ans19 = input("Where would you like to investigate A: The flowers B: The greenhouse C: The Widower: ") 
     if ans19 == "A":
            print("You have chosen to investigate the flowers. You will now roll to see how well you investigate")
            magnifying, evidence =Roll(magnifying, evidence)
     elif ans19 == "B":
            print("You have chosen to investigate the greenhouse. You will now roll to see how well you investigate")
            flashlight, evidence =Roll(flashlight, evidence)
     elif ans19 == "C":
            print("You have chosen to investigate the widower. You will now roll to see how well you investigate")
            book, evidence =Roll(book, evidence)
     print("You may now enter three different rooms. 1: The Tennis court 2: The garage 3: The Office")
     ans98 = input("Where would you like to enter ")


if ans12 == "2":
     print("You have entered the Roof")
     ans27 = input("Where would you like to investigate A: The bar B: The observatory C: The Gentleman: ") 
     if ans27 == "A":
            print("You have chosen to investigate the Bar. You will now roll to see how well you investigate")
            dna, evidence =Roll(dna, evidence)
     elif ans27 == "B":
            print("You have chosen to investigate the observatory. You will now roll to see how well you investigate")
            flashlight, evidence =Roll(flashlight, evidence)
            print("You may now enter three different rooms. 1: The Tennis court 2: The garage 3: The Office")
            asn98 = input("Where would you like to enter")
     elif ans27 == "C":
            print("You have chosen to investigate the Gentleman. You will now roll to see how well you investigate")
            book, evidence =Roll(book, evidence)
            print("You may now enter three different rooms. 1: The Tennis court 2: The garage 3: The Office")
     asn98 = input("Where would you like to enter")
if ans12 == "3":
     print("You have entered the Pool")
     ans45 = input("Where would you like to investigate A: The locker room B: The pool C: The poolboy: ")   
     if ans45 == "A":
            print("You have chosen to investigate the locker room. You will now roll to see how well you investigate")
            flashlight, evidence =Roll(flashlight, evidence)
     elif ans45 == "B":
            print("You have chosen to investigate the pool. You will now roll to see how well you investigate")
            dna, evidence =Roll(dna, evidence)
     elif ans45 == "C":
            print("You have chosen to investigate the poolboy. You will now roll to see how well you investigate")
            book, evidence =Roll(book, evidence)
     print("You may now enter three different rooms. 1: The Tennis court 2: The garage 3: The Office")
     ans98 = input("Where would you like to enter ")





if ans98 == "1":
    print("You have entered the tennis court")
    ans65 = input("Where would you like to investigate A: The net B: The rackets: ")   
    if ans65 == "A":
            print("You have chosen to investigate the Net. You will now roll to see how well you investigate")
            flashlight, evidence =Roll(flashlight, evidence)
    elif ans65 == "B":
            print("You have chosen to investigate the rackets. You will now roll to see how well you investigate")
            dna, evidence =Roll(dna, evidence)

if ans98 == "2": 
    print("You have entered the garage")
    ans93 = input("Where would you like to investigate A: The car B: The staircase C: The mechanic: ")   
    if ans93 == "A":
            print("You have chosen to investigate the car. You will now roll to see how well you investigate")
            flashlight, evidence =Roll(flashlight, evidence)
    elif ans93 == "B":
            print("You have chosen to investigate the staircase. You will now roll to see how well you investigate")
            dna, evidence =Roll(dna, evidence)


if ans98 == "3":
    print("You have entered the office")
    ans25 = input("Where would you like to investigate A: The desk B: The drawer: ")   
    if ans25 == "A":
            print("You have chosen to investigate the desk. You will now roll to see how well you investigate")
            magnifying, evidence =Roll(magnifying, evidence)
    elif ans25 == "B":
            print("You have chosen to investigate the drawer. You will now roll to see how well you investigate")
            magnifying, evidence =Roll(magnifying, evidence)

print("You will now confront the killer")
print("You have ", evidence, "Evidence")
y = random.randint(0, 100)
print("would you like to accuse someone? Y or N")
ans71 = input("Your answer: ")
y+= 20*evidence

if ans71 == ("FAX") and evidence == 0:
            print("You become lord of fax machines and ascend")

if ans71 == ("N"):
            print("You do not accuse anyone and go home.")
            print("THE END")
if ans71 == ("Y"):
            print("You accuse someone")
            if y>70:
                  print("and they turn out to be the killer")
            elif evidence == 3:
                  print("You use evidence to find the killer")
            elif evidence>1:
                  print("Despite having evidence you are unable to convince people that you found the killer")
            else:
                  print("You are unable to convince someone and you are now under investigation")
print("The end")
            




      

  
      
