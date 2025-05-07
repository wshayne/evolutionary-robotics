from suppress_stdout import stdout_redirected
from suppress_stdout import stderr_redirected
with stderr_redirected():
    from simulation import SIMULATION

def simulate(brain, d_gui, target, ab):
    with stdout_redirected():
        simulation = SIMULATION(d_gui, brain, target, ab)

        simulation.Run()

    return simulation.Get_Fitness()