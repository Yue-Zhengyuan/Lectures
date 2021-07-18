import numpy as np
import os
from itertools import product
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.lines as lines
from matplotlib import animation

plt.style.use('default')
# plt.style.use('dark_background')
dir_path = os.path.dirname(os.path.realpath(__file__))

fig, ax = plt.subplots(figsize=(8,3))
# fig, ax = plt.subplots()
ax.set_aspect(1)
# set axis limit
ax.set_ylim(-0.5, 3)
ax.set_xlim(-1.5, 12)
# set axes width
for key in ax.spines:
    ax.spines[key].set_linewidth(1)
# remove unnecessary axes
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
# set axes to go across the origin
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
# remove ticks
ax.set_xticks([])
ax.set_yticks([])

# motion parameters
## linear velocity of CM
v = 1
## wheel radius
r = 1
## spin angular velocity
w = v / r

def cm(t):
    """position of wheel CM"""
    return np.array([
        v * t, r
    ])

def ref_to_cm(t):
    """reference point position relative to wheel CM"""
    return r * np.array([
        np.cos(3*np.pi/2 - w * t),
        np.sin(3*np.pi/2 - w * t)
    ])

# draw path (cycloid) of the reference point
time = np.linspace(0, 5*np.pi, 300)
cycloid = np.asarray([cm(t) + ref_to_cm(t) for t in time])
ax.plot(*cycloid.T, color='blue', linewidth=0.8)

# plot the wheel at a given time t0
for i in range(5):
    t0 = 4*i * np.pi / 5
    wheel_kw = dict(linewidth=1, edgecolor='black',fill=False)
    if i == 1:
        wheel = patches.Circle(cm(t0), radius=r, **wheel_kw)
    else:
        wheel = patches.Circle(cm(t0), radius=r, linestyle='--', **wheel_kw)
    ax.add_artist(wheel)
    line_kw = dict(linewidth=1)
    refvec = cm(t0)+ref_to_cm(t0)
    refline = lines.Line2D([cm(t0)[0], refvec[0]], [cm(t0)[1], refvec[1]], color='red', **line_kw)
    ax.add_artist(refline)
    refline2 = lines.Line2D([cm(t0)[0], cm(t0)[0]], [0, cm(t0)[1]], color='black', linestyle='--', **line_kw)
    ax.add_artist(refline2)

# add text
text_kw = dict(fontsize=14, transform=ax.transAxes)
ax.text(0.95, 0.03, '$x$', text_kw)
ax.text(0.08, 0.9, '$y$', text_kw)
ax.text(0.08, 0.03, 'O', text_kw)
ax.text(0.26, 0.03, '$x_{CM}(t)$', text_kw)
ax.text(0.23, 0.35, r'$\varphi(t)$', text_kw)

plt.show()
fig.savefig(dir_path + '/cycloid.svg')
