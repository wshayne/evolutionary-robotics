import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import time

if __name__ == '__main__':
    start = time.time()
    phc = PARALLEL_HILL_CLIMBER()
    phc.Evolve()
    end = time.time() 
    phc.Show_Best()
    print(end - start)