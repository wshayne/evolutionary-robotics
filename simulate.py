from simulation import SIMULATION

def simulate(brain, d_gui):

    simulation = SIMULATION(d_gui, brain)

    simulation.Run()

    return simulation.Get_Fitness()