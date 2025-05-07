from solution import SOLUTION
import simulate
import constants as c
import copy
import os
import numpy as np
import multiprocessing as mp
class PARALLEL_HILL_CLIMBER:
    def __init__(self, ab):
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
            self.parents[i] = SOLUTION(ab)
        self.true_fitnesses = []
        self.evaluated_fitnesses = []
    
    def Evolve(self):
        # self.Evaluate(self.parents)
        for i in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
            if i%10 == 0:
                self.evaluated_fitnesses.append(self.Evaluate(self.parents, [[0, 0], [3, 0], [-3, 0], [0, 3], [0, -3], [3, 3], [3, -3], [-3, 3], [-3, -3]]))

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        positions = np.random.uniform(-5, 5, (5, 2))
        self.true_fitnesses.append(self.Evaluate(self.parents, positions))
        self.Evaluate(self.children, positions)
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}
        for i in self.parents:
            self.children[i] = copy.deepcopy(self.parents[i])

    def Mutate(self):
        for c in self.children:
            self.children[c].Mutate()
    
    def Evaluate(self, solutions, positions):
        # test_pos = [[3, 0], [-3, 0]]
        # test_pos = np.random.uniform(-5, 5, (5, 2))
        with mp.Pool(16) as p:
            res = []
            for pos in positions:
                res.append(p.starmap(SOLUTION.Evaluate, [(s, "DIRECT", pos) for s in solutions.values()]))
        fitnesses = np.sum(res, axis=0)
        for f, s in zip(fitnesses, solutions.values()):
            s.fitness = f
        return fitnesses

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
        simulate.simulate(self.parents[min_p].brain, "GUI", [3, 0], self.ab)
        simulate.simulate(self.parents[min_p].brain, "GUI", [-3, 0], self.ab)
        self.parents[min_p].Create_Brain()
    
    def Save_Brains(self, prefix=""):
        for i, p in enumerate(self.parents.values()):
            p.Create_Brain(filename=f"{prefix}brain{i}.nndf")
    
    def Save_Fitness_History(self, prefix=""):
        np.save(f"{prefix}true_fitnesses.npy", self.true_fitnesses)
        np.save(f"{prefix}evaluated_fitnesses.npy", self.evaluated_fitnesses)