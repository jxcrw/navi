#!/usr/bin/python
"""matplotlib demo."""
# Jak Crow
# Created: 2018/02/05

import pickle
import time
import matplotlib.pyplot as plt
from test import split_dict

# def load_stocks(universe):
#     stock_data_path = r'C:\Users\jak\ALL\DV\Stocks\data\\' + universe + '.p'
#     load_start = time.time()
#     print(f"Loading {universe} data...", end="", flush=True)
#     stocks = pickle.load(open(stock_data_path, 'rb'))
#     print(f"finished in {round((time.time() - load_start), 2)} seconds")
#     return stocks

# universe = 'S&P 500' # All US Stocks, NYSE, NASDAQ, Russell 3000, S&P 1500, or S&P 500
# stock_universe = load_stocks(universe)

# apple = stock_universe['AAPL']

# plt.figure(1)
# plt.plot(apple.Close)
# plt.xlabel('Date')
# plt.ylabel('Price')
# plt.legend()

# plt.figure(2)
# # Moar data etc.
# plt.show()
# # plt.savefig('graph.png', dpi=1000)

# # ─────────────────────────────────────────────────────────────────────────────
# # https://matplotlib.org/gallery/mplot3d/2dcollections3d.html#sphx-glr-gallery-mplot3d-2dcollections3d-py
# from mpl_toolkits.mplot3d import Axes3D
# import numpy as np
# import matplotlib.pyplot as plt

# fig = plt.figure()
# ax = fig.gca(projection='3d')

# # Plot a sin curve using the x and y axes.
# x = np.linspace(0, 1, 100)
# y = np.sin(x * 2 * np.pi) / 2 + 0.5
# ax.plot(x, y, zs=0, zdir='z', label='curve in (x,y)')

# # Plot scatterplot data (20 2D points per colour) on the x and z axes.
# colors = ('r', 'g', 'b', 'k')

# # Fixing random state for reproducibility
# np.random.seed(19680801)

# x = np.random.sample(20 * len(colors))
# y = np.random.sample(20 * len(colors))
# c_list = []
# for c in colors:
#     c_list.extend([c] * 20)
# # By using zdir='y', the y value of these points is fixed to the zs value 0
# # and the (x,y) points are plotted on the x and z axes.
# ax.scatter(x, y, zs=0, zdir='y', c=c_list, label='points in (x,z)')

# # Make legend, set axes limits and labels
# ax.legend()
# ax.set_xlim(0, 1)
# ax.set_ylim(0, 1)
# ax.set_zlim(0, 1)
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')

# # Customize the view angle so it's easier to see that the scatter points lie
# # on the plane y=0
# ax.view_init(elev=20., azim=-35)

# plt.show()

# # ─────────────────────────────────────────────────────────────────────────────

# # https://matplotlib.org/gallery/mplot3d/scatter3d.html#sphx-glr-gallery-mplot3d-scatter3d-py
# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt
# import numpy as np

# # Fixing random state for reproducibility
# np.random.seed(19680801)


# def randrange(n, vmin, vmax):
#     '''
#     Helper function to make an array of random numbers having shape (n, )
#     with each number distributed Uniform(vmin, vmax).
#     '''
#     return (vmax - vmin)*np.random.rand(n) + vmin

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# n = 100

# # For each set of style and range settings, plot n random points in the box
# # defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
# for c, m, zlow, zhigh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
#     xs = randrange(n, 23, 32)
#     ys = randrange(n, 0, 100)
#     zs = randrange(n, zlow, zhigh)
#     ax.scatter(xs, ys, zs, c=c, marker=m)

# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')

# plt.show()

# # ─────────────────────────────────────────────────────────────────────────────

# # https://stackoverflow.com/questions/17756925/how-to-plot-heatmap-colors-in-3d-in-matplotlib

# import numpy as np
# from pylab import *
# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt

# def randrange(n, vmin, vmax):
#     return (vmax-vmin)*np.random.rand(n) + vmin

# fig = plt.figure(figsize=(8,6))

# ax = fig.add_subplot(111,projection='3d')
# n = 100

# xs = randrange(n, 23, 32)
# ys = randrange(n, 0, 100)
# zs = randrange(n, 0, 100)

# colmap = cm.ScalarMappable(cmap=cm.hsv)
# colmap.set_array(zs)

# yg = ax.scatter(xs, ys, zs, c=cm.hsv(zs/max(zs)), marker='o')
# cb = fig.colorbar(colmap)

# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')


# plt.show()

# ─────────────────────────────────────────────────────────────────────────────

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca(projection='3d')

# Plot a sin curve using the x and y axes.
x = np.linspace(0, 1, 100)
y = np.sin(x * 2 * np.pi) / 2 + 0.5
ax.plot(x, y, zs=0, zdir='z', label='curve in (x,y)')

# Plot scatterplot data (20 2D points per colour) on the x and z axes.
colors = ('r', 'g', 'b', 'k')

# Fixing random state for reproducibility
np.random.seed(19680801)

x = np.random.sample(20 * len(colors))
y = np.random.sample(20 * len(colors))
c_list = []
for c in colors:
    c_list.extend([c] * 20)
# By using zdir='y', the y value of these points is fixed to the zs value 0
# and the (x,y) points are plotted on the x and z axes.
ax.scatter(x, y, zs=0, zdir='y', c=c_list, label='points in (x,z)')

# Make legend, set axes limits and labels
ax.legend()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Customize the view angle so it's easier to see that the scatter points lie
# on the plane y=0
ax.view_init(elev=20., azim=-35)

plt.show()
