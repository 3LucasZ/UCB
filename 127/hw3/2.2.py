import os
from matplotlib import pyplot as plt
import numpy as np

dir = os.path.dirname(os.path.abspath(__file__))
# Load matrix
matrix = np.loadtxt(os.path.join(dir, "2.1.csv"), delimiter=',')
n = matrix.shape[0] // 2
l1_err = matrix[:n, :]
l2_err = matrix[n:, :]
print(l1_err)
print(l2_err)
t_set = np.arange(-2, 2.1, 0.1)

# Find coordinates for red / blue points
red_1 = []
red_2 = []
blue_1 = []
blue_2 = []
for t1i in range(n):
    t1 = t_set[t1i]
    for t2i in range(n):
        t2 = t_set[t2i]
        if l1_err[t1i, t2i] < l2_err[t1i, t2i]:
            red_1.append(t1)
            red_2.append(t2)
        else:
            blue_1.append(t1)
            blue_2.append(t2)
print(len(red_1), len(blue_1))

# Plot points
plt.figure(figsize=(8, 8))
plt.scatter(red_1, red_2,
            c='red', label='$l_1$ smaller error')
plt.scatter(blue_1, blue_2, c='blue',
            label='$l_2$ smaller error')
plt.xlabel('$t_1$')
plt.ylabel('$t_2$')
plt.title('Grid of Estimator Error Comparisons')
plt.legend()
plt.grid(False)
plt.savefig(os.path.join(dir, 'grid.png'))
