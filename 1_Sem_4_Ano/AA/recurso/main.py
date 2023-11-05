from graph_generator import GraphGenerator
from exhaustive_search import exhaustive_search
from greedy_search import greedy_search
from random_search import random_search
import matplotlib.pyplot as plt
import math

#nvertices=[i for i in range(2,51)]
n = 200
e = exhaustive_search()
g = greedy_search()
r = random_search()
""" 
for n in nvertices:
    g= GraphGenerator(n)
    g.generate_graph("graphs/")
"""
e_file = open("basic_ops_singles.txt", "w") 
g_file = open("time_sinles.txt", "w")
r_file = open("configurations_singles.txt", "w")  

#for n in nvertices:
vertices = []
f = open(f"graphs/_{n}")
for line in f:
    x,y,waste = line.split(' ')
    vertices.append((int(x),int(y)))

num_of_warehouses = [k for k in range(2,n)]
for k in num_of_warehouses:
    if all(k%i!=0 for i in range(2,k)): #check for prime number
        #eSol, e_b_ops, e_time, e_tests = e.min_largest_distance(vertices,k)
        
        #rSol, r_b_ops, r_time, r_tests = r.min_largest_distance(vertices,k, 10)
        gSol, g_b_ops, g_time = g.min_largest_distance(vertices,k)
        
        e_file.write(f"{len(vertices),k}  {g_b_ops}\n")
        g_file.write(f"{len(vertices),k} {g_time}\n")
        #r_file.write(f"{len(vertices),k}  {g_tests}\n")
        
    