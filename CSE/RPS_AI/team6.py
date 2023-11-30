'''The function move(my_history, their_history) must return 'r', 'p', or 's'.
my_history and their_history are strings of the same length, perhaps length zero.
'''
import random
strategy_name = 'winStayLoseShift'

def move(my_history, their_history):
    if len(their_history)==0: #start with paper
       my_move = 'p' 
    else:
        #if they choose rock, I lose, otherwise, I win/tie
        if(their_history[-1] != "r"):
            my_move = 'p'
        else:
            my_move = random.choice(["r", "s"]) 
    return my_move
    


        
