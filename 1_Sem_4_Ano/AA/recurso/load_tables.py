from math import sqrt
import random
import time
from itertools import combinations
import itertools
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

a = open("basic_ops.txt","r")
curx = 0

counter = 0
f = ""
b = []
c = []
d = []
k = [2,3,5,7,11,13,17]
n = []
n2 = []
for line in a:
    #print(line)
    if counter == 0:
        counter += 1
        continue

    x,y, exh, g, rand = line.split(" ")
    x = x[1:-1]
    y = y[:-1]

    if y == '5':
        n.append(int(x))
        n2.append(factorial(n))
        b.append(int(exh))
        c.append(int(g))
        d.append(int(rand))
    """if int(x) % 2 != 0:
        continue
    #print( int(x),int(y), exh, g, rand)
    if curx == 0:
        curx = x
      
    elif curx == x:
       
            if y != "2":
                if y != "3":
                    f = f+" "+g
    else: 
        print(str(int(x)-2)+" "+f)
        curx = x
        f = ""
     
        if y != "2":
            if y != "3":
                f = f+x+" "+g"""
print(b)
print(c)
print(d)
print(n)


        
    
    