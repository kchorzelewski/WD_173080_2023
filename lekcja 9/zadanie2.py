import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

n = 50

for c, m, zlow, zhigh in [('r', 'o', -50, -25), ('b', '>', -30, -5), ('y', '1', -60, -2), ('g', 'h', -5, -30), ('b', 's', -30, -8)]:
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 100)
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c=c, marker=m)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()

