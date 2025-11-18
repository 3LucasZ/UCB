import cvxpy as cp
import numpy as np

# setup optimization problem
x = cp.Variable(3)
y = cp.Variable(3)
obj = cp.Minimize(cp.sum_squares(x - y))
constraints = [
    # S1
    cp.sum_squares(x) <= 3,
    cp.sum(x) >= 0.5,
    # S2
    cp.sum_squares(y) <= 30,
    cp.sum(y) >= 9
]
prob = cp.Problem(obj, constraints)
sol = prob.solve()

# (i) Minimum distance > 0 IFF S1 and S2 do not intersect
print(f"Minimum distance: {sol:.4f}")
if (sol > 0):
    print("by (i) we have that minimum distance > 0 IFF S1 and S2 do not intersect.")
    print("since minimum distance is indeed > 0, this implies that S1 and S2 do not intersect.")
x_star = x.value
y_star = y.value
print(f"x*: {np.round(x_star, 4)}")
print(f"y*: {np.round(y_star, 4)}")

# (ii) The separating hyperplane:
# contains point (x* + y*) / 2
# and has normal vector a = (y* - x*)
# H = {aTz = b | z}
a = y_star - x_star
midpoint = (x_star + y_star) / 2
b = a.T @ midpoint

print("By (ii) we have that a separating hyperplane H can be found that contains the midpoint of x* and y* and has normal vector (y* - x*).")
print("Separating hyperplane: H = {aTx=b | x}")
print(f"a: {np.round(a, 4)}")
print(f"b: {b:.4f}")
print(f"{a[0]:.2f}*x1 + {a[1]:.2f}*x2 + {a[2]:.2f}*x3 = {b:.2f}")
