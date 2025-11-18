import numpy as np
from itertools import combinations
import time


def experiment(n=40, m=5):
    A = np.random.uniform(low=-1.0, high=1.0, size=(m, n))
    b = np.random.uniform(low=-1.0, high=1.0, size=m)

    # Iterate through all C(n, m) combinations of m hyperplanes
    vertex_count = 0
    hyperplane_set = range(n)
    for hyperplane_subset in combinations(hyperplane_set, m):
        G = A[:, list(hyperplane_subset)]
        # Find intersection of the hyperplanes
        x = np.linalg.solve(G, b)
        # check feasibility of potential vertex x
        if np.all(x >= 0):
            vertex_count += 1
    print("Experiment finished, found:", vertex_count)
    return vertex_count


k = 10
cnt = sum([experiment() for _ in range(k)])
ret = cnt/k
print("Average # of vertices over 10 runs:", ret)

'''
Experiment finished, found: 25609
Experiment finished, found: 24793
Experiment finished, found: 19045
Experiment finished, found: 12780
Experiment finished, found: 21220
Experiment finished, found: 25642
Experiment finished, found: 27078
Experiment finished, found: 21739
Experiment finished, found: 20372
Experiment finished, found: 14349
Average # of vertices over 10 runs: 21262.7
'''
