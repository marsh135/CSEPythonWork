import random
import matplotlib.pyplot as plt #graph
import numpy as np #graph

rolls = int(input("Please enter a number of rolls: "))
           
def roller(rolls):
    
    ones = 0
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    sixes = 0
    for number in range(rolls):
        result = random.randint(1,6)
        if result == 1:
            print(rolls, "One")
            ones +=1
        elif result == 2:
            print(rolls, "Two")
            twos +=1
        elif result == 3:
            print(rolls, "Three")
            threes +=1
        elif result == 4:
            print(rolls, "Four")
            fours +=1
        elif result == 5:
            print(rolls, "Five")
            fives +=1      
        else:
            print(rolls, "Six!")
            sixes +=1
    print("Ones: " + str(ones) + "   Twos: " + str(twos) + 
          "     Threes: " + str(threes) + "   Fours: " + str(fours) +
          "    Fives: " + str(fives) + "   Sixes: " + str(sixes))
    
    labelledList = ['Ones', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes']
    print(labelledList)
    
    #graph = np.array([ones, twos, threes, fours, fives, sixes]) #graph
    #plt.pie(graph)#graph
    #plt.show()#graph
    records = [ones, twos, threes, fours, fives, sixes]
    print(records)
    fig, ax = plt.subplots()
    ax.pie(records, labels=labelledList, autopct='%1.1f%%')
    plt.show()

roller(rolls)