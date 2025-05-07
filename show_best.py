import numpy as np
from pyrosim.neuralNetwork import NEURAL_NETWORK
from simulate import simulate

def get_best(files):
    min_fit = np.inf
    for i, f in enumerate(files):
        fitnesses = np.load(f)
        if np.min(fitnesses[-1]) < min_fit:
            min_file = i
            min_index = np.argmin(fitnesses[-1])
            min_fit = np.min(fitnesses[-1])
    return min_file, min_index

def show_brain(file, target, ab):
    brain = NEURAL_NETWORK(file)
    simulate(brain, "GUI", target, ab)

a_files, b_files = [[f"results/fitness/{i}{ab}_evaluated_fitnesses.npy" for i in range(20)] for ab in ['a', 'b']]

a_best_run, a_best_index = get_best(a_files)
b_best_run, b_best_index = get_best(b_files)

# show_brain(f"results/brains/{a_best_run}a/brain{a_best_index}.nndf", [0, -3], 'a')

# show_brain(f"results/brains/{b_best_run}b/brain{b_best_index}.nndf", [0, -3], 'b')

show_brain("brain50112.nndf", [0, -3], 'b')