import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import pickle
import time

def run(i, ab):
    phc = PARALLEL_HILL_CLIMBER(ab)
    phc.Evolve()
    with open(f'results/climber/{i}{ab}.pickle', 'wb') as f:
        pickle.dump(phc, f)
    os.mkdir(f"results/brains/{i}{ab}")
    phc.Save_Brains(prefix=f"results/brains/{i}{ab}/")
    phc.Save_Fitness_History(f"results/fitness/{i}{ab}_")

def continue_run(i, ab):
    with open(f'results/climber/{i}{ab}.pickle', 'rb') as f:
        phc = pickle.load(f)
    phc.Evolve()
    with open(f'results/climber/{i+10}{ab}.pickle', 'wb') as f:
        pickle.dump(phc, f)
    os.mkdir(f"results/brains/{i+10}{ab}")
    phc.Save_Brains(prefix=f"results/brains/{i+10}{ab}/")
    phc.Save_Fitness_History(f"results/fitness/{i+10}{ab}_")

if __name__ == '__main__':
    for i in range(10):
        for ab in ['a', 'b']:
            continue_run(i, ab)