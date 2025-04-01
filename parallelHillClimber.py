from solution import SOLUTION
import simulate
import constants as c
import copy
import os
import numpy as np
import multiprocessing as mp
class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        try:
            os.remove("world.sdf")
        except:
            pass
        try:
            os.remove("body.urdf")
        except:
            pass
        SOLUTION.Create_Body()
        SOLUTION.Create_World()
        self.parents = {}
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION()
    
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

    def Mutate(self):
        for c in self.children:
            self.children[c].Mutate()
    
    def Evaluate(self, solutions):
        test_pos = [[3, 0], [-3, 0]]
        with mp.Pool(16) as p:
            res = []
            for pos in test_pos:
                res.append(p.starmap(SOLUTION.Evaluate, [(s, "DIRECT", pos) for s in solutions.values()]))
        fitnesses = np.sum(res, axis=0)
        for f, s in zip(fitnesses, solutions.values()):
            s.fitness = f

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
        simulate.simulate(self.parents[min_p].brain, "GUI", [3, 0])
        simulate.simulate(self.parents[min_p].brain, "GUI", [-3, 0])
        self.parents[min_p].Create_Brain()