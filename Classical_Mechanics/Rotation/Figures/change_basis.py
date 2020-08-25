"""
    Adapted from the StackOverflow answer
    https://stackoverflow.com/a/63568715/10444934
"""

from matplotlib import pyplot as plt
from matplotlib.backend_bases import MouseButton
from matplotlib.ticker import MultipleLocator
from matplotlib.patches import Polygon
import numpy as np

fig, ax = plt.subplots(figsize=(10,7))
text_kw = dict(fontsize=14)
picked_artist = None

ax.set_xlim(-5, 5)
ax.set_ylim(-1, 6)
ax.set_aspect(1)
# ax.xaxis.set_major_locator(MultipleLocator(1))
# ax.xaxis.set_minor_locator(MultipleLocator(0.5))
# ax.yaxis.set_major_locator(MultipleLocator(1))
# ax.yaxis.set_minor_locator(MultipleLocator(0.5))

ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
ax.tick_params(left=False, bottom=False, labelsize=14)
ax.text(4.5, -0.5, '$x$', **text_kw)
ax.text(-0.5, 5.5, '$y$', **text_kw)

ax.grid(True, which='major', linestyle='-', lw=1)
# ax.grid(True, which='minor', linestyle=':', lw=0.5)

def vecNewBasis(v, e1, e2):
    """Find components of v along e1, e2"""
    matD = np.array([e1, e2])
    return np.dot(np.linalg.inv(matD.T), v)

def vecLabelXY(v, start=(0,0)):
    """Determine the position of the vector label"""
    raise NotImplementedError
    # midpoint = tuple((v[i] + start[i])/2 for i in range(2))
    # # direction orthogonal to v
    # coord = midpoint
    # return coord

# locator of vectors
init_e1, init_e2, init_v = (1,0), (0,1), (3,2)
pt1, = ax.plot(*init_e1, '+', color='red', ms=10, picker=20)
pt2, = ax.plot(*init_e2, '+', color='blue', ms=10, picker=20)
ptv, = ax.plot(*init_v, '+', color='green', ms=10, picker=20)
# basis vector and its label
# use empty annotation as arrow
e1 = ax.annotate('', (0, 0), init_e1, ha="left", va="center",
        arrowprops=dict(arrowstyle='<|-', lw=2, fc="red", ec="red", shrinkA=0, shrinkB=0))
label_e1 = ax.text(*(1.2*np.array(e1.xyann)), '$e_1$', **text_kw, color='red')
e2 = ax.annotate('', (0, 0), init_e2, ha="left", va="center",
        arrowprops=dict(arrowstyle='<|-', lw=2, fc="blue", ec="blue", shrinkA=0, shrinkB=0))
label_e2 = ax.text(*(1.2*np.array(e2.xyann)), '$e_2$', **text_kw, color='blue')

# arbitrary vector
v = ax.annotate('', (0, 0), init_v, ha="left", va="center",
        arrowprops=dict(arrowstyle='<|-', lw=2, fc="green", ec="green", shrinkA=0, shrinkB=0))
label_v = ax.text(*(1.1*np.array(v.xyann)), '$v$', **text_kw, color='green')

# display standard components of e1, e2
coord_e1 = ax.text(-4.5, 5.5, 
    '$e_1$: ({:.3f}, {:.3f})'.format(*np.array(e1.xyann)), 
    **text_kw, color='red'
)
coord_e2 = ax.text(-4.5, 5, 
    '$e_2$: ({:.3f}, {:.3f})'.format(*np.array(e2.xyann)), 
    **text_kw, color='blue'
)
# standart components of v
coord_v = ax.text(-4.5, 4, 
    '$v$ (standard): \n({:.3f}, {:.3f})'.format(*np.array(v.xyann)), 
    **text_kw, color='green'
)
# components of v along e1, e2
vNew = vecNewBasis(np.array(v.xyann), np.array(e1.xyann), np.array(e2.xyann))
comp_v = ax.text(-4.5, 3, 
    '$v$ (along $e_1,e_2$): \n({:.3f}, {:.3f})'.format(*vNew), 
    **text_kw, color='green'
)

# auxiliary lines
verts = [np.array([0,0]), vNew[0]*np.array(e1.xyann),
        np.array(v.xyann), vNew[1]*np.array(e2.xyann),]
aux = Polygon(verts, linestyle='--', linewidth=1, edgecolor='black', fill=False)
ax.add_artist(aux)

def on_pick(event):
    'called when an element is picked'
    global picked_artist
    if event.mouseevent.button == MouseButton.LEFT:
        picked_artist = event.artist

def on_button_release(event):
    'called when a mouse button is released'
    global picked_artist
    if event.button == MouseButton.LEFT:
        picked_artist = None

def on_motion_notify(event):
    'called when the mouse moves'
    global picked_artist, aux
    if picked_artist is not None and event.inaxes is not None and event.button == MouseButton.LEFT:
        picked_artist.set_data([event.xdata], [event.ydata])
        if picked_artist == pt1:
            e1.set_position([event.xdata, event.ydata])
            label_e1.set_position(1.2 * np.array([event.xdata, event.ydata]))
        elif picked_artist == pt2:
            e2.set_position([event.xdata, event.ydata])
            label_e2.set_position(1.2 * np.array([event.xdata, event.ydata]))
        elif picked_artist == ptv:
            v.set_position([event.xdata, event.ydata])
            label_v.set_position(1.1 * np.array([event.xdata, event.ydata]))
        # update coordinates and components
        vNew = vecNewBasis(np.array(v.xyann), np.array(e1.xyann), np.array(e2.xyann))
        coord_e1.set_text('$e_1$: ({:.3f}, {:.3f})'.format(*np.array(e1.xyann)))
        coord_e2.set_text('$e_2$: ({:.3f}, {:.3f})'.format(*np.array(e2.xyann)))
        coord_v.set_text('$v$ (standard): \n({:.3f}, {:.3f})'.format(*np.array(v.xyann)))
        comp_v.set_text('$v$ (along $e_1,e_2$): \n({:.3f}, {:.3f})'.format(*vNew))
        # remove parallelogram and redraw
        aux.remove()
        verts = [np.array([0,0]), vNew[0]*np.array(e1.xyann),
                np.array(v.xyann), vNew[1]*np.array(e2.xyann),]
        aux = Polygon(verts, linestyle='--', linewidth=1, edgecolor='black', fill=False)
        ax.add_artist(aux)
        fig.canvas.draw_idle()

fig.canvas.mpl_connect('button_release_event', on_button_release)
fig.canvas.mpl_connect('pick_event', on_pick)
fig.canvas.mpl_connect('motion_notify_event', on_motion_notify)

plt.show()