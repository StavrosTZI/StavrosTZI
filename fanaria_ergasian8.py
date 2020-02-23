import random
arithmepan=int(input("Αριθμός Επαναλήψεων:"))
fanA=random.randrange(0,20)
fanB=random.randrange(0,20)
fanC=random.randrange(0,20)
autokin=[fanA,fanB,fanC]
"""
Το άνω όριο για τον αριθμό των αυτοκινήτων (20) θα μπορούσε να είναι το 
οποιοσδήποτε θετικός ακέραιος ή να μην υπάρχει 
"""
epan=1  
while epan<=arithmepan:
    print ("Επανάληψη: " , epan)#Ελεγχω ποιο ειναι το φαναρι με τα περισσοτερα αυτοκινητα
    if fanA>fanB:
        if fanA>fanC:
            green=0  
    if fanB>fanC:
        if fanB>fanA:
            green=1
    if fanC>fanB:
        if fanC>fanA:
            green=2
    if fanA==fanB and fanA>fanC:
        pinv=[0,1]
        green=random.choice(pinv)
    if fanA==fanC and fanA>fanC:
        pinv=[0,2]
        green=random.choice(pinv)
    if fanB==fanC and fanB>fanA:
        pinv=[1,2]
        green=random.choice(pinv)   
    if fanA==fanB and fanA==fanC:
        pinv=[1,2,3]                
        green=random.choice(pinv)
    if green==0:
        newca=random.randrange(5,10)#newca:new cars
        if newca>fanA:
            newca=fanA
            """
            Εάν ο τυχαίος αριθμός τον αυτοκινήτων που φεύγουν απο το φανάρι ειναι μεγαλύτερος απο τον 
            αριθμό των αυτοκινητων στο φανάρι θεωρώ οτι ολα τα αυτοκίνητα φέυγουν απο το φανάρι
            """
        print("Το φανάρι Α είναι πράσινο ")
        print("Στο φανάρι Α υπάρχουν ",fanA ," και φεύγουν απο το φανάρι ",newca,"αυτοκίνητα" )
        fanA=fanA-newca
        newca=random.randrange(0,5)
        print("Το φανάρι Β είναι κόκκινο")
        print("Στο φανάρι Β υπάρχουν ",fanB,"αυτοκίνητα και έρχονται ",newca," νέα αυτοκίνητα")
        fanB=fanB+newca
        newca=random.randrange(0,5)
        print("Το φανάρι Γ είναι κόκκινο")
        print(" Στο φανάρι Γ υπάρχουν ",fanC," αυτοκίνητα και έρχονται ",newca," νέα αυτοκίνητα ")
        fanC=fanC+newca
    if green==1:
        newca=random.randrange(5,10)
        if newca>fanB:
            newca=fanB
        print("Το φανάρι Β είναι πράσινο")
        print("Στο φανάρι Β υπάρχουν ",fanB," αυτοκίνητα και φέυγουν ",newca," αυτοκίνητα " )
        fanB=fanB-newca
        newca=random.randrange(0,5)
        print("Το φανάρι Α είναι κόκκινο")
        print(" Στο φανάρι A υπάρχουν ",fanA," αυτοκίνητα και έρχονται ",newca," νέα αυτοκίνητα ")
        fanA=fanA+newca
        newca=random.randrange(0,5)
        print("Το φανάρι Γ είναι κόκκινο")
        print(" Στο φανάρι Γ υπάρχουν ",fanC," αυτοκίνητα και έρχονται ",newca," νέα αυτοκίνητα ")
        fanC=fanC+newca
    if green==2:
        newca=random.randrange(5,10)
        if newca>fanB:
            newca=fanB
        print("Το φανάρι Γ είναι πράσινο")
        print("Στο φανάρι Γ υπάρχουν ",fanC," αυτοκίνητα και φέυγουν ",newca," αυτοκίνητα " )
        fanC=fanC-newca
        newca=random.randrange(0,5)
        print("Το φανάρι Α είναι κόκκινο")
        print(" Στο φανάρι A υπάρχουν ",fanA," αυτοκίνητα και έρχονται ",newca," νέα αυτοκίνητα ")
        fanA=fanA+newca
        newca=random.randrange(0,5)
        print("Το φανάρι Β είναι κόκκινο")
        print(" Στο φανάρι Β υπάρχουν ",fanB," αυτοκίνητα και έρχονται ",newca," νέα αυτοκίνητα ")
        fanΒ=fanB+newca
    epan=epan+1    