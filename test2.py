#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 03:49:07 2020

@author: POWERPUFFGIRLS
"""
import random
queue = []
goal_state = (5,0)



# x = current[0] = 7
# y = current[1] = 3
current = (0,0)
queue.append(current)
while goal_state not in queue:
    selection = random.randint(0, 7)

    if current == (7,3)  and (7,0) in queue and (0,3) in queue:
        print('Whole process needs to be backtracked.')
        #Since there is no possible moves such as pouring 3 or 7 because they are already added to queue
        #Current situation is a dead-end for our process.
        current = (0,0)
        queue = [current]
        
    if selection == 0 and current[0] < 7 and ((7,current[1]) not in queue):
        current = (7,current[1])
        queue.append(current)
        print("Fill up 7. current: ",current, "added")
            
    elif selection == 1 and current[1] <3 and ((current[0],3) not in queue):
        current = (current[0],3)
        queue.append(current)
        print("Fill up 3. current: ",current, "added")
            
    elif selection == 2 and current[0] >0 and ((0,current[1]) not in queue):
        current = (0,current[1])
        queue.append(current)
        print("Pour 7. current: ",current, "added")
            
    elif selection == 3 and current[1] >0 and ((current[0],0) not in queue):
        current = (current[0],0)
        queue.append(current)
        print("Pour 3. current: ",current, "added")
            
    elif selection == 4 and (current[0] + current[1] <= 7 and current[1] >0) and ((current[0] + current[1],0) not in queue):
        current = (current[0] + current[1],0)
        queue.append(current)
        print("Pour 3 to 7, fitted. current: ",current, "added")
        
    elif selection == 5 and (current[0] + current[1] > 7 and current[0] < 7) and ((7,current[0] + current[1] -7) not in queue):
        current = (7,current[0] + current[1] -7) 
        queue.append(current)
        print("Pour 3 to 7, fitted. Remained in 3: ",current, "added")
            
    elif selection == 6 and( current[0] + current[1] <= 3 and current[0] > 0) and ((0,current[0] + current[1]) not in queue):
        current= (0,current[0] + current[1])
        queue.append(current)
        print("Pour 7 to 3, fitted. current: ",current, "added")
            
    elif selection == 7 and (current[0] + current[1] > 3 and current[1] <3) and ((current[0] + current[1] -3,3) not in queue):
        current = (current[0] + current[1] -3,3)
        queue.append(current)
        print("Pour 7 to 3, remained in 7. current: ",current, "added")
        