from solution import SOLUTION
import constants as c
import multiprocessing as mp
from pyrosim.neuralNetwork import NEURAL_NETWORK
from simulate import simulate

# s = SOLUTION()

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

brain = NEURAL_NETWORK("brain90517.nndf")

print(simulate(brain, "GUI", [-3, 0]))