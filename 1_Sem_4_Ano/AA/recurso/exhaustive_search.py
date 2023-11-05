from itertools import combinations
import time
import numpy as np


class exhaustive_search:

    def min_largest_distance(self, vertices, k):
        start_time = time.time()
        best_combination = None
        min_largest_distance = float('inf')
        # Create a list of all possible combinations of k vertices
        basic_ops = 0
        for combination in combinations(vertices, k):
            #print(combination)
            distances = []
            for vertex in vertices:
                closest_distance = float('inf')
                for chosen_vertex in combination:
                    #print(vertex)
                    #print(chosen_vertex)
                    if vertex == chosen_vertex:
                        continue
                    distance = np.linalg.norm(np.array(vertex) - np.array(chosen_vertex))
                    basic_ops += 1
                    if distance < closest_distance:
                        closest_distance = distance
                distances.append(closest_distance)
            largest_distance = max(distances)
            if largest_distance < min_largest_distance:
                min_largest_distance = largest_distance
                best_combination = combination

      
        return best_combination, basic_ops, time.time() - start_time, 

#vertices = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 2)]
#k = 3

#print(min_largest_distance(vertices, k))
