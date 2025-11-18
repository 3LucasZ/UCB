import cvxpy as cp
import numpy as np


c = np.array([5, -7, 10, 3, -1])
A = np.array([
    [-1, -3,  3, -1, -2],
    [2, -5,  3, -2, -2],
    [0,  1, -1, -1,  1]
])
b = np.array([0, 3, -2])

x_LP = cp.Variable(5)
constraints_LP = [
    A @ x_LP <= b,
    x_LP >= 0,
    x_LP <= 3
]
objective_LP = cp.Maximize(c @ x_LP)
prob_LP = cp.Problem(objective_LP, constraints_LP)
opt_LP = prob_LP.solve()
x_star_LP = x_LP.value
print(
    f"LP solution: x* = {list(map('{:.8f}'.format, x_star_LP))} => {opt_LP:.8f}")
'''
LP solution: x* = ['3.00000000', '0.00000000', '3.00000000', '3.00000000', '2.99999999'] => 50.99999999
'''


'''
NOTE: OPTIONAL IP solution checker (NOT PART OF PART ii/iii) that I did just for fun / sanity checking my discussion logic!!
Please do not dock me points off for this :0
'''
x_IP = cp.Variable(5, integer=True)
constraints_IP = [
    A @ x_IP <= b,
    x_IP >= 0,
    x_IP <= 3
]
objective_IP = cp.Maximize(c @ x_IP)
prob_IP = cp.Problem(objective_IP, constraints_IP)
opt_IP = prob_IP.solve()
x_star_IP = x_IP.value
print(
    f"IP solution: x* = {list(map('{:.8f}'.format, x_star_IP))} => {opt_IP:.8f}")


difference = opt_LP - opt_IP
print(f"Objective optimality difference: {opt_LP - opt_IP}")
