from solution import SOLUTION
import constants as c
import copy
import os
import numpy as np

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
    
    def Evolve(self):
        self.Evaluate(self.parents)
        for _ in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}
        for i in self.parents:
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for c in self.children:
            self.children[c].Mutate()
    
    def Evaluate(self, solutions):
        for p in solutions:
            solutions[p].Start_Simulation("DIRECT")
        for p in solutions:
            solutions[p].Wait_For_Simulation_To_End()

    def Select(self):
        for p in self.parents:
            if self.parents[p].fitness > self.children[p].fitness:
                self.parents[p] = self.children[p]
    
    def Print(self):
        print()
        for p in self.parents:
            print(self.parents[p].fitness, self.children[p].fitness)
        print()
    
    def Show_Best(self):
        min_fit = np.inf
        min_p = 0
        for p in self.parents:
            if self.parents[p].fitness < min_fit:
                min_fit = self.parents[p].fitness
                min_p = p
        self.parents[min_p].Start_Simulation("GUI")