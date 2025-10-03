import os
import cvxpy as cp
import numpy as np

dir = os.path.dirname(os.path.abspath(__file__))

A = np.array([[1, 1, 1],
              [-1, 1, 0],
              [-1, -1, 1],
              [1, 0, 1],
              [-1, 1, 1],
              [0, -1, 1]])
x_star = np.array([1, 1, 1])
t_set = np.arange(-2, 2.1, 0.1)

n = len(t_set)
l1_err = np.zeros((n, n))
l2_err = np.zeros((n, n))
for t1i in range(n):
    t1 = t_set[t1i]
    for t2i in range(n):
        t2 = t_set[t2i]
        v = np.array([t1, 0, 0, 0, t2, 0])
        b = A @ x_star + v
        for k in [1, 2]:
            x = cp.Variable(3)
            obj = cp.Minimize(cp.norm(A @ x - b, k))
            prob = cp.Problem(obj)
            prob.solve()
            err = cp.norm(x.value - x_star, 2)
            if k == 1:
                l1_err[t1i, t2i] = err.value
            else:
                l2_err[t1i, t2i] = err.value

matrix = np.vstack((l1_err, l2_err))
np.savetxt(os.path.join(dir, '2.1.csv'), matrix, delimiter=',')
