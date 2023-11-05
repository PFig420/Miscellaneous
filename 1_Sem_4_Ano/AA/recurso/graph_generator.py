
import random
import math


class GraphGenerator:

    def __init__(self, nvertices):
        self.nvertices=nvertices
        random.seed(97487)


    def generate_graph(self, outfile):

            axis_values= [[i, j] for i in range(1,1000) for j in range(1,1000)]
            filename=f'{outfile}_{self.nvertices}'
            outf = open(filename , "w")
            
            for i in range(self.nvertices):
                coord=random.choice(axis_values)
                axis_values.remove(coord)

                #don't allow verticies too close
                if [coord[0]-1, coord[1]] in axis_values:
                    axis_values.remove([coord[0]-1, coord[1]]) 

                if [coord[0]+1, coord[1]] in axis_values:
                    axis_values.remove([coord[0]+1, coord[1]]) 

                if [coord[0], coord[1]-1] in axis_values:
                    axis_values.remove([coord[0], coord[1]-1]) 

                if [coord[0], coord[1]+1] in axis_values:
                    axis_values.remove([coord[0], coord[1]+1]) 

                outf.write(f'{coord[0]} {coord[1]} \n')

n=200
g= GraphGenerator(n)
g.generate_graph("graphs/")