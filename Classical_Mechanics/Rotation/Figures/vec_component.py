import numpy as np
import os
from itertools import product
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.lines as lines

plt.style.use('default')
# plt.style.use('dark_background')
dir_path = os.path.dirname(os.path.realpath(__file__))
solution = False

fig, ax = plt.subplots(figsize=(6,6))
# set axis limit
ax.set_aspect(1)
ax.set_ylim(-3, 3)
ax.set_xlim(-3, 3)
# remove ticks
ax.set_xticks([])
ax.set_yticks([])

# style for text
text_kw = dict(fontsize=14, transform=ax.transAxes)

# standard basis
basis_e = np.eye(2)

# components of arbitrary basis a1, a2 along standard basis
arrow_kw = {'head_width': 0.1, 'head_length': 0.2, 'width': 0.01, 'length_includes_head': True}
basis_a = np.array([
    [np.cos(np.pi/6), np.sin(np.pi/6)],
    [np.cos(3*np.pi/4), np.sin(3*np.pi/4)]
])

# components of vector v along a1, a2
v = np.array([1.5, 2.])
# components of vector v along standard basis
v_e = np.zeros((2,))
for i in range(2):
    v_e += v[i] * basis_a[i]
ax.add_artist(patches.FancyArrow(
    0, 0, *v_e, color='blue', **arrow_kw
)) 

# auxiliary lines: 
# vectors v0 a0 and v1 a1
va_color = ['lightcoral','lightgreen']
for i in range(2):
    ax.add_artist(patches.FancyArrow(
        0, 0, *(v[i] * basis_a[i]), color=va_color[i], **arrow_kw
    ))
    ax.add_artist(patches.FancyArrow(
        *(v[(i+1)%2] * basis_a[(i+1)%2]), *(v[i] * basis_a[i]), 
        color=va_color[i], **arrow_kw
    ))
# draw basis vector
a_color = ['red', 'green']
for i in range(2):
    ax.add_artist(patches.FancyArrow(
        0, 0, *basis_a[i], color=a_color[i], **arrow_kw
    ))

plt.show()