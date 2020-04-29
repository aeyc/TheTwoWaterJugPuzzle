#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 05:30:24 2020

@author: POWERPUFFGIRLS
"""
#Optional part to use code with different values
#import getopt
#
#args = str(input())
#args = args.split()
#args = args[1:]
#
##test --m M --n N --d D
#opts,args = getopt.getopt(args, "m:n:d:", ['m=', 'n=','d='])
#for i in opts:
#    if i[0] == '--m':
#        m = int(i[1])
#    elif i[0] == '--n':
#        n = int(i[1])
#    elif i[0] == '--d':
#        d = int(i[1])
d = 5
m = 3
n = 7
#%% Algorithm 1's methods  
def gcd(a, b): 
    if b==0: 
        return a 
    return gcd(b, a%b)

def step2(m,n,d,k):
    c = 0
    while k!= d and k <=n:
        print(k,"+(",m, ") ->", k+m)
        k +=m
        c+=1
    return k,c

def step3(m,n,d,k):
    c = 0
    while k>n:
        print(k,"-(",n, ") ->",k-n)
        k = k-n
    c+=1
    return k,c
#%% Algorithm 2's methods
def step2_2(m,n,d,k):
    c = 0
    if k != d:
        print(k,"+(",n, ") ->", k+n)
        k = k + n
        c+=1
    return k,c

def step3_2(m,n,d,k):
    c = 0
    while k != d and k>=m:
        print(k,"-(",m, ") ->",k-m)
        k = k-m
        c+=1
    return k,c
#%%
if m > 0 and n > m  and d < n and gcd(m,n) == 1:
#Algorithm 1
#Step 1. Initialize a dummy variable k = 0.
    k = 0
    x = 0
    y =0
    print('Corresponding integer sequence:')
#Step 2. If k != d, then repeat adding m to k and assign the result to k until k = d or k > n.
    if k!= d:
        k,x = step2(m,n,d,k)
#Step 3. If k > n, then subtract n from k and assign the result to k.
    if  k>n:
        k,y = step3(m,n,d,k)
#Step 4. If k = d, then stop. Otherwise, repeat the steps from Step 2 to Step 4. 
    new_x = 0
    new_y = 0
    while k != d:
        k,new_x = step2(m,n,d,k)
        x+=new_x
        if k == d:
            break
        else:
            if k >n:
                k,new_y = step3(m,n,d,k)
                y+=new_y
    print("For the first algorithm,")
    print("We got the equation:\n(m={})*(x={}) + (n={})*(-y=-{}) = d = {}.".format(m,x,n,y,d))
    print()
    
#Algorithm 2
#Step 1. Initialize a dummy variable k = 0.
    k = 0
    x = 0
    y =0
#Step 2. If k != d, then add n to k and assign the result to k. 
    if k!= d:
        k,x = step2_2(m,n,d,k)
        
#Step 3. If k > d, then repeat subtracting m from k and assign the result to k until k =d or k < m.
    if  k>d:
        k,y = step3_2(m,n,d,k)
#Step 4. If k = d, then stop. Otherwise, repeat the steps from Step 2 to Step 4.
    new_x = 0
    new_y = 0
    while k != d:
        k,new_x = step2_2(m,n,d,k)
        x+=new_x
        if k == d:
            break
        else:
            if k > d:
                k,new_y = step3_2(m,n,d,k)
                y+=new_y
    
    print("For the second algorithm,")
    print("We got the equation:\n(m={})*(-x=-{}) + (n={})*(y={}) = d = {}.".format(m,y,n,x,d))
    
else:
    print("According to the procedure, 0<m<n and d<n and gcd(m,n) should be equal to 1")