import random
import time
import numpy as np
class random_search:
    def min_largest_distance(self, vertices, k, iterations):
        start_time = time.time()
        final_vertices = None
        min_largest_distance = float('inf')
        basic_ops = 0
        
        for i in range(iterations):
            random_vertices = random.sample(vertices, k)
            
            distances = []
            for vertex in vertices:
                closest_distance = float('inf')
                for chosen_vertex in random_vertices:
                    distance = np.linalg.norm(np.array(vertex) - np.array(chosen_vertex))
                    basic_ops += 1
                    if distance < closest_distance:
                        closest_distance = distance
                distances.append(closest_distance)
            largest_distance = max(distances)
            if largest_distance < min_largest_distance:
                min_largest_distance = largest_distance
                final_vertices = random_vertices
        return final_vertices, basic_ops, time.time() - start_time, iterations