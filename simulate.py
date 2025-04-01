from simulation import SIMULATION

def simulate(brain, d_gui, target):

    simulation = SIMULATION(d_gui, brain, target)

    simulation.Run()

    return simulation.Get_Fitness()