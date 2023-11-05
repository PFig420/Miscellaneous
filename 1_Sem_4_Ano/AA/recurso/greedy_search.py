import time
import numpy as np


class greedy_search:
    def min_largest_distance(self,vertices, k):
        temp = vertices.copy()
        final_solution = []
        start_time = time.time()
        basic_ops = 0
       
        while len(final_solution) < k:
            furthest_distance = 0
            furthest_vertices = [None, None]
            for i in range(len(temp)):
                for j in range(i+1, len(temp)):
                    distance = np.linalg.norm(np.array(temp[i]) - np.array(temp[j]))# dummy distance calculation
                    basic_ops +=1
                    if distance > furthest_distance:
                        furthest_distance = distance
                        furthest_vertices = [temp[i], temp[j]]
            if len(final_solution) == k - 1:
                final_solution.append(furthest_vertices[0])
            else:
                final_solution.append(furthest_vertices[0])
                final_solution.append(furthest_vertices[1])
            temp.remove(furthest_vertices[0])
            temp.remove(furthest_vertices[1])
       
        return final_solution, basic_ops, time.time() - start_time
