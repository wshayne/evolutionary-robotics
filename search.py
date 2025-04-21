import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import pickle
import time

if __name__ == '__main__':
    start = time.time()
    phc = PARALLEL_HILL_CLIMBER()
    phc.Evolve()
    end = time.time() 
    phc.Show_Best()
    print(end - start)
    with open('climber.pickle', 'wb') as f:
        pickle.dump(phc, f)