import numpy as np
import cvxpy as cp
import matplotlib.pyplot as plt

N = 1000
k = 5
x_star = np.zeros(N)
x_star[9] = 5
x_star[19] = -2
x_star[94] = 7
x_star[749] = 15
x_star[919] = -10

m_probs = []
m_values = range(5, 101)
trials = 10
for m in range(5, 101):
    success = 0
    for _ in range(trials):
        A = np.random.randn(m, N)
        y = A @ x_star
        x_hat = cp.Variable(N)
        objective = cp.Minimize(cp.norm(x_hat, 1))
        constraints = [A @ x_hat == y]
        problem = cp.Problem(objective, constraints)
        problem.solve()
        error = np.linalg.norm(x_hat.value - x_star, 1)
        if error < 0.01:
            success += 1
    p_m = success / trials
    m_probs.append(p_m)
    if (m % 10 == 0):
        print("Done: m =", m, "p(m) =", p_m)

# plot
plt.plot(m_values, m_probs)
plt.title(f'Compressed Sensing Recovery ($N={N}$, $k={k}$)')
plt.xlabel('Num measurements m')
plt.ylabel('Empirical prob of success p(m)')
plt.yticks(np.arange(0, 1.1, 0.1))
plt.show()

'''
Done: m = 10 p(m) = 0.0
Done: m = 20 p(m) = 0.0
Done: m = 30 p(m) = 0.4
Done: m = 40 p(m) = 0.5
Done: m = 50 p(m) = 1.0
Done: m = 60 p(m) = 1.0
Done: m = 70 p(m) = 1.0
Done: m = 80 p(m) = 1.0
Done: m = 90 p(m) = 1.0
Done: m = 100 p(m) = 1.0
'''
