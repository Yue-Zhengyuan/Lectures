"""
    Demostration of change of basis
    ===============================

    Drag the basis vectors to see how the components
    of an arbitrary vector change

    Adapted from the StackOverflow answer
    https://stackoverflow.com/a/63568715/10444934
"""

from matplotlib import pyplot as plt
from matplotlib.backend_bases import MouseButton
from matplotlib.ticker import MultipleLocator
from matplotlib.patches import Polygon, FancyArrow
import numpy as np

fig, ax = plt.subplots(figsize=(10,7))
text_kw = dict(fontsize=14)
picked_artist = None

ax.set_title('Change of Basis Demostration', fontsize=16)

ax.set_xlim(-5, 5)
ax.set_ylim(-1, 6.5)
ax.set_aspect(1)
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.xaxis.set_minor_locator(MultipleLocator(0.5))
ax.yaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_minor_locator(MultipleLocator(0.5))

ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
ax.tick_params(left=False, bottom=False, labelsize=14)
ax.text(4.5, -0.5, '$x$', **text_kw)
ax.text(-0.5, 5.5, '$y$', **text_kw)

ax.grid(True, which='major', linestyle='-', lw=1)
ax.grid(True, which='minor', linestyle=':', lw=0.5)

def vecNewBasis(v, e1, e2):
    """Find components of v along e1, e2"""
    matD = np.array([e1, e2])
    return np.dot(np.linalg.inv(matD.T), np.array(v))

def vecLabelXY(v, start=(0,0)):
    """Determine the position of the vector label"""
    raise NotImplementedError
    # midpoint = tuple((v[i] + start[i])/2 for i in range(2))
    # # direction orthogonal to v
    # coord = midpoint
    # return coord

# locator of vectors
init_e1, init_e2, init_v = np.array([3,1]), np.array([-1,2]), np.array([2,3])
pt1, = ax.plot(*init_e1, '+', color='red', ms=10, picker=20)
pt2, = ax.plot(*init_e2, '+', color='blue', ms=10, picker=20)
ptv, = ax.plot(*init_v, '+', color='green', ms=10, picker=20)
# basis vector and its label
# use empty annotation as arrow
arrow_kw = {'head_width': 0.2, 'head_length': 0.3, 'width': 0.03, 'length_includes_head': True}
# e1 = ax.annotate('', (0, 0), init_e1, ha="left", va="center",
#         arrowprops=dict(arrowstyle='<|-', lw=2, fc="red", ec="red", shrinkA=0, shrinkB=0))
e1 = FancyArrow(0, 0, *init_e1, **arrow_kw, color='red')
label_e1 = ax.text(*(1.1*init_e1), '$e_1$', **text_kw, color='red')
# e2 = ax.annotate('', (0, 0), init_e2, ha="left", va="center",
#         arrowprops=dict(arrowstyle='<|-', lw=2, fc="blue", ec="blue", shrinkA=0, shrinkB=0))
e2 = FancyArrow(0, 0, *init_e2, **arrow_kw, color='blue')
label_e2 = ax.text(*(1.1*init_e2), '$e_2$', **text_kw, color='blue')

# arbitrary vector
# v = ax.annotate('', (0, 0), init_v, ha="left", va="center",
#         arrowprops=dict(arrowstyle='<|-', lw=2, fc="green", ec="green", shrinkA=0, shrinkB=0))
v = FancyArrow(0, 0, *init_v, **arrow_kw, color='green')
label_v = ax.text(*(1.1*init_v), '$v$', **text_kw, color='green')
ax.add_artist(e1)
ax.add_artist(e2)
ax.add_artist(v)

# display standard components of e1, e2
coord_e1 = ax.text(-4.5, 5.5, 
    '$e_1$: ({:.3f}, {:.3f})'.format(*init_e1), 
    **text_kw, color='red'
)
coord_e2 = ax.text(-4.5, 5, 
    '$e_2$: ({:.3f}, {:.3f})'.format(*init_e2), 
    **text_kw, color='blue'
)
# standart components of v
coord_v = ax.text(-4.5, 4, 
    '$v$ (standard): \n({:.3f}, {:.3f})'.format(*init_v), 
    **text_kw, color='green'
)
# components of v along e1, e2
vNew = vecNewBasis(init_v, init_e1, init_e2)
comp_v = ax.text(-4.5, 3, 
    '$v$ (along $e_1,e_2$): \n({:.3f}, {:.3f})'.format(*vNew), 
    **text_kw, color='green'
)

# auxiliary lines
verts = [np.array([0,0]), vNew[0]*init_e1,
        init_v, vNew[1]*init_e2,]
aux = Polygon(verts, linestyle='--', linewidth=1, edgecolor='black', fill=False)
ax.add_artist(aux)
# grid along basis vectors
alpha = np.linspace(-10,10,10)
grid1, grid2 = [], []
for n in range(-10,10):
    ## parallel to e1
    line1 = np.transpose(np.array([a * init_e1 + n * init_e2 for a in alpha]))
    ## parallel to e2
    line2 = np.transpose(np.array([a * init_e2 + n * init_e1 for a in alpha]))
    grid1.append(ax.plot(line1[0], line1[1], color='cornflowerblue', zorder=0)[0])
    grid2.append(ax.plot(line2[0], line2[1], color='cornflowerblue', zorder=0)[0])

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
    global picked_artist
    global init_e1, init_e2, init_v
    global e1, e2, v, aux
    global grid1, grid2
    if picked_artist is not None and event.inaxes is not None and event.button == MouseButton.LEFT:
        picked_artist.set_data([event.xdata], [event.ydata])
        if picked_artist == pt1 or picked_artist == pt2:
            if picked_artist == pt1:
                # redraw arrow e1
                init_e1 = np.array([event.xdata, event.ydata])
                e1.remove()
                e1 = FancyArrow(0, 0, *init_e1, **arrow_kw, color='red')
                ax.add_artist(e1)
                label_e1.set_position(1.1 * init_e1)
            elif picked_artist == pt2:
                # redraw arrow e2
                init_e2 = np.array([event.xdata, event.ydata])
                e2.remove()
                e2 = FancyArrow(0, 0, *init_e2, **arrow_kw, color='blue')
                ax.add_artist(e2)
                label_e2.set_position(1.1 * init_e2)
            # redraw gridlines
            for line1, line2 in zip(grid1, grid2):
                line1.remove()
                line2.remove()
            grid1.clear()
            grid2.clear()
            for n in range(-10,10):
                ## parallel to e1
                line1 = np.transpose(np.array([a * init_e1 + n * init_e2 for a in alpha]))
                ## parallel to e2
                line2 = np.transpose(np.array([a * init_e2 + n * init_e1 for a in alpha]))
                grid1.append(ax.plot(line1[0], line1[1], color='cornflowerblue', zorder=0)[0])
                grid2.append(ax.plot(line2[0], line2[1], color='cornflowerblue', zorder=0)[0])
        elif picked_artist == ptv:
            # redraw arrow v
            init_v = np.array([event.xdata, event.ydata])
            v.remove()
            v = FancyArrow(0, 0, *init_v, **arrow_kw, color='green')
            ax.add_artist(v)
            label_v.set_position(1.1 * init_v)
        # update coordinates and components
        vNew = vecNewBasis(init_v, init_e1, init_e2)
        coord_e1.set_text('$e_1$: ({:.3f}, {:.3f})'.format(*init_e1))
        coord_e2.set_text('$e_2$: ({:.3f}, {:.3f})'.format(*init_e2))
        coord_v.set_text('$v$ (standard): \n({:.3f}, {:.3f})'.format(*init_v))
        comp_v.set_text('$v$ (along $e_1,e_2$): \n({:.3f}, {:.3f})'.format(*vNew))
        # remove parallelogram and redraw
        aux.remove()
        verts = [np.array([0,0]), vNew[0]*init_e1,
                init_v, vNew[1]*init_e2,]
        aux = Polygon(verts, linestyle='--', linewidth=1, edgecolor='black', fill=False)
        ax.add_artist(aux)
        fig.canvas.draw_idle()

fig.canvas.mpl_connect('button_release_event', on_button_release)
fig.canvas.mpl_connect('pick_event', on_pick)
fig.canvas.mpl_connect('motion_notify_event', on_motion_notify)

plt.show()