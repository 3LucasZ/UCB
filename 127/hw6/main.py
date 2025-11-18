import cvxpy as cp
import numpy as np
import random

x1 = cp.Variable(1)
x2 = cp.Variable(1)
constraints = [
    x1 >= 0,
    x2 >= 0,
    x1 + 4 * x2 <= 4,
    4 * x1 + x2 <= 4
]
n = 200
solutions = []

for _ in range(n):
    # Get random pair (a, b) from [-1, 1]
    a = random.uniform(-1, 1)
    b = random.uniform(-1, 1)

    # Solve LP and store solution
    objective = cp.Minimize(a * x1 + b * x2)
    prob = cp.Problem(objective, constraints)
    prob.solve()
    sol = (round(float(x1.value), 4), round(float(x2.value), 4))
    solutions.append(sol)

# Analysis
unique, counts = np.unique(solutions, axis=0, return_counts=True)
print("Empirically discovered vertices of the feasible set:")
for u, c in zip(unique, counts):
    print(f"{u} occurs with {c/n:.3f} empirical probability")
