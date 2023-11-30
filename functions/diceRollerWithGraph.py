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
    for number in range(1, rolls+1):
        result = random.randint(1,6)
        if result == 1:
            print(number, "One")
            ones +=1
        elif result == 2:
            print(number, "Two")
            twos +=1
        elif result == 3:
            print(number, "Three")
            threes +=1
        elif result == 4:
            print(number, "Four")
            fours +=1
        elif result == 5:
            print(number, "Five")
            fives +=1      
        else:
            print(number, "Six!")
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
    ax.pie(records, labels=labelledList, autopct='%1.2f%%')
    plt.show()

roller(rolls)



import matplotlib.pyplot as plt
'''
plt.plot([1,2,3,5], [1, 4, 9, 16], 'go')

plt.ylabel('Some Numbers:')
plt.xlabel('Your Name')
plt.show()


import numpy as np

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

'''











