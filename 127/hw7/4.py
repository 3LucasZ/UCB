import cvxpy as cp
import numpy as np

# Warehouse costs
C = np.array([
    [20, 25, 20],  # W1
    [10, 30, 40],  # W2
    [90, 80, 70]   # W3
])
# Supply
s = np.array([40, 30, 90])
# Demand
d = np.array([30, 30, 30])
# Edge weights
X = cp.Variable((3, 3))
# Minimize warehouse costs
objective = cp.Minimize(cp.sum(cp.multiply(C, X)))
# Constraints
constraints = [
    X >= 0,
    # Supply constraints
    cp.sum(X, axis=1) <= s,
    # Demand constraints
    cp.sum(X, axis=0) == d
]
# Solve
prob = cp.Problem(objective, constraints)
min_cost = prob.solve()
print(f"Min Cost: {min_cost:.3f}")
X_star = X.value
print("     C1          C2          C3")
print(f"W1: {list(map('{:.3f}'.format, X_star[0, :]))}")
print(f"W2: {list(map('{:.3f}'.format, X_star[1, :]))}")
print(f"W3: {list(map('{:.3f}'.format, X_star[2, :]))}")
'''
    Min Cost: 2650.000
        C1          C2          C3
    W1: ['0.000', '30.000', '10.000']
    W2: ['30.000', '0.000', '0.000']
    W3: ['0.000', '0.000', '20.000']
'''
