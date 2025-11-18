
import matplotlib.pyplot as plt
import numpy as np


def plotFn(p, k):
    '''
    graph Fn(x), the CDF of the capacities of BSC(p) channels polarized n=2^k times
    '''
    n = 2**k
    ps = [p]
    for _ in range(k):
        new_ps = []
        for p in ps:
            p_l = 2*p - p*p
            p_r = p*p
            new_ps.extend([p_l, p_r])
        ps = new_ps
    Cs = [1-p for p in ps]
    x = np.sort(Cs)
    y = np.arange(1, n + 1) / n
    plt.step(x, y, where='post', label=f"k={k}")


if __name__ == "__main__":
    p = 0.5
    C = 1-p
    plotFn(p, 5)
    plotFn(p, 10)
    plotFn(p, 20)
    # Expect 1-C useless, C perfect channels
    plt.axhline(y=1-C, c="r", label="cutoff")
    plt.xlabel("Polarized channel capacity")
    plt.ylabel("CDF")
    plt.title(
        f"Fn(x) for n=2^k polarized channels of BSC(p={p})")
    plt.legend()
    # plt.show()
    plt.savefig("f_dist.jpg")
