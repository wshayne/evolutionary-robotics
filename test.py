from solution import SOLUTION
import constants as c
import multiprocessing as mp
from pyrosim.neuralNetwork import NEURAL_NETWORK
from simulate import simulate
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import os

s = SOLUTION('b')
s.Create_Brain()

# print(s.brain.synapses)
# print(s.weights)

# s.Mutate()

# print(s.brain.synapses)
# print(s.weights)

# for ((source, target), synapse) in s.brain.synapses.items():
#     assert s.brain.synapses[source, target].weight == s.weights[int(source), int(target) - c.numSensorNeurons]

# def add_one(list):
#     for i in range(len(list)):
#         list[i] += 1
#     return list

# if __name__ == '__main__':
#     with mp.Pool(4) as p:
#         lists = [[j for _ in range(j)] for j in range(4)]
#         print(lists)
#         print(p.map(add_one, lists))
#         print(lists)

#brain = NEURAL_NETWORK("brain76141.nndf")
# brain = NEURAL_NETWORK("brain70674.nndf")

# print(simulate(brain, "GUI", [0, -3]))

# if __name__ == "__main__":
#     phc = PARALLEL_HILL_CLIMBER("a")
#     phc.Evolve_For_One_Generation()
#     os.mkdir("test_brains")
#     phc.Save_Brains("test_brains/")