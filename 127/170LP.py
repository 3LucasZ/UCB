import cvxpy as cp
import numpy as np

A = np.array([
    [-10,  3,  3],  # Your 'rock' payoffs
    [4, -1, -3],  # Your 'paper' payoffs
    [6, -9,  2]   # Your 'scissors' payoffs
])

print("Row Player's LP (Maximizer)")
p = cp.Variable(3, name="p")
v = cp.Variable(name="v")
constraints_row = [
    A.T @ p >= v,
    cp.sum(p) == 1,
    p >= 0
]
objective_row = cp.Maximize(v)
problem_row = cp.Problem(objective_row, constraints_row)
problem_row.solve()
print(f"z: {v.value:.4f}")
print(f"p1:{p.value[0]:.4f}")
print(f"p2:{p.value[1]:.4f}")
print(f"p3:{p.value[2]:.4f}")


print("Column Player's LP (Minimizer)")
q = cp.Variable(3, name="q")
w = cp.Variable(name="w")
constraints_col = [
    A @ q <= w,
    cp.sum(q) == 1,
    q >= 0
]
objective_col = cp.Minimize(w)
problem_col = cp.Problem(objective_col, constraints_col)
problem_col.solve()
print(f"z: {w.value:.4f}")
print(f"q1: {q.value[0]:.4f}")
print(f"q2: {q.value[1]:.4f}")
print(f"q3: {q.value[2]:.4f}")
