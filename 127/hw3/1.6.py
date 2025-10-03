import os
import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt

dir = os.path.dirname(os.path.abspath(__file__))

# Constants
A = np.array([[2, 0, 0],
              [- 1, 1, 0],
              [- 1, -1, 1]])
B = np.array([-1, -1, 1])
# H = np.hstack([A@A@A@B, A@A@B, A@B, B])
xd = np.array([3, 2, 2])


def getTraj(useSafety):
    # Variables
    u = cp.Variable(4)
    xs = cp.Variable((3, 5))

    # Constraints
    constraints = [xs[:, 0] == 0]
    for k in range(0, 3+1):
        constraints.append(xs[:, k+1] == A@xs[:, k] + B*u[k])
    constraints.append(xs[:, 4] == xd)
    if useSafety:
        constraints.extend([-3.3 <= xs, xs <= 3.2])

    # Solve
    obj = cp.Minimize(cp.sum_squares(u))
    prob = cp.Problem(obj, constraints)
    prob.solve(canon_backend="SCIPY")

    # Display results
    print("useSafety:", useSafety)
    print("status:", prob.status)
    print("optimal energy:", prob.value)
    print("optimal input:")
    print(u.value)
    np.set_printoptions(linewidth=np.inf)
    print("optimal trajectory:")
    print(xs.value)
    return xs.value


# Display results
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
xs1 = getTraj(False)
xs2 = getTraj(True)
ax.plot3D(xs1[0, :], xs1[1, :], xs1[2, :],
          color='blue', marker='o', linestyle='--', label='unbounded')
ax.plot3D(xs2[0, :], xs2[1, :], xs2[2, :],
          color='red', marker='o', linestyle='--', label='with safety net')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
d = 3
ax.set_xlim(-d, d)
ax.set_ylim(-d, d)
ax.set_zlim(-d, d)
ax.set_title('Optimal Trajectories')
plt.legend()
plt.savefig(os.path.join(dir, "traj12.png"))
