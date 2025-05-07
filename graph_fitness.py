import matplotlib.pyplot as plt
import numpy as np

def graph_evaluated():
    fig, ax = plt.subplots(1, 2)

    for i in range(10, 20):
        try:
            f = np.load(f"results/fitness/{i}a_evaluated_fitnesses.npy")
        except:
            break
        f_avg = np.mean(f, axis=1)
        f_min = np.min(f, axis=1)
        lines = ax[0].plot([*range(1, 102, 10), *range(102, 203, 10)], f_avg)
        # lines = ax[0].plot([*range(1, 102, 10), *range(102, 203, 10)], f_min)
        
        try:
            f = np.load(f"results/fitness/{i}b_evaluated_fitnesses.npy")
        except:
            lines += ax[1].plot([], [], c="b")
            break
        f_avg = np.mean(f, axis=1)
        f_min = np.min(f, axis=1)
        lines += ax[1].plot([*range(1, 102, 10), *range(102, 203, 10)], f_avg)
        # lines += ax[1].plot([*range(1, 102, 10), *range(102, 203, 10)], f_min)

    ax[0].set_title("Average Fitness (A)")
    ax[1].set_title("Average Fitness (B)")
    # ax.legend(lines, ["a", "b"])
    plt.show()

def graph_actual():
    fig, ax = plt.subplots(1, 2)
    for i in range(10, 19):
        for ab in ['a', 'b']:
            f = np.load(f"results/fitness/{i}{ab}_true_fitnesses.npy")
            graph_actual_file(f, ax, ab)
    ax[0].set_title("Average Fitness (A)")
    ax[1].set_title("Average Fitness (B)")
    plt.show()

def graph_actual_file(f, ax, ab):
    if ab == 'a':
        i = 0
    elif ab == 'b':
        i = 1
    f_avg = np.mean(f, axis=1)
    ax[i].plot(f_avg)

if __name__ == "__main__":
    graph_evaluated()
    # graph_actual()