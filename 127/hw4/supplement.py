import numpy as np

G = np.array([[100, 90, 100, 80, 70],
              [80, 70, 60, 70, 80],
              [60, 50, 40, 50, 60]])

U, s, Vt = np.linalg.svd(G)

u1 = -1 * U[:, :1]
s1 = s[0]
vt1 = -1 * Vt[:1, :]
B = s1 * u1 @ vt1
print(u1, s1, vt1)
print(B)
print([(float)(1/yi) for yi in vt1[0]])
