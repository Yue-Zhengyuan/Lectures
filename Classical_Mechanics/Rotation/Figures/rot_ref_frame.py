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

# motion parameters
## orbital angular velocity
w_orbit = 1
## orbit radius
r = 3
## spin angular velocity
w_spin = 10
## square edge length
edge = 2
## distance of XY origin to square center
a = edge / 4

def sq_center(t):
    """square center position"""
    return r * np.array([
        np.cos(w_orbit * t), 
        np.sin(w_orbit * t)
    ])

def center_to_corner(t):
    """square left-lower corner position relative to center"""
    return edge / np.sqrt(2) * np.array([
        np.cos(5*np.pi/4 + w_spin * t),
        np.sin(5*np.pi/4 + w_spin * t)
    ])

def center_to_oriXY(t):
    """XY origin position relative to square center"""
    return a * np.array([
        np.cos(w_spin * t),
        np.sin(w_spin * t),
    ])

# set up plot
fig, ax = plt.subplots(figsize=(5,5))

def init():
    ax.cla()
    ## set axis limit
    ax.set_ylim(-5, 5)
    ax.set_xlim(-5, 5)
    ## set axes width
    for key in ax.spines:
        ax.spines[key].set_linewidth(1.5)
    ## remove unnecessary axes
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ## set axes to go across the origin
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ## remove ticks
    ax.set_xticks([])
    ax.set_yticks([])
    # time as parameter
    time = np.linspace(-np.pi, np.pi, 300)
    # draw path of the square center
    ax.plot(*sq_center(time), color='green', linestyle='--')
    # draw path of the XY origin
    ax.plot(*(sq_center(time) + center_to_oriXY(time)), color='red', linestyle='--')

# animate for specific time t0
def animate(t0):
    """Animate the motion of spinning square, with time t0 as parameter"""
    # t0 = (40/180) * np.pi
    init()
    # draw square center at t0
    # artist_list = []
    arrow_kw = {'head_width': 0.2, 'head_length': 0.3, 'width': 0.03, 'length_includes_head': True}
    arr_center = patches.FancyArrow(*([0,0]), *sq_center(t0), color='green', **arrow_kw)
    ax.add_artist(arr_center)
    # artist_list.append(ax.add_artist(arr_center))

    # draw XY axes at t0
    ori_XY = sq_center(t0) + center_to_oriXY(t0)
    arr_X = patches.FancyArrow(*ori_XY, *np.array([1.5, 0]), color='red', **arrow_kw)
    arr_Y = patches.FancyArrow(*ori_XY, *np.array([0, 1.5]), color='red', **arrow_kw)
    ax.add_artist(arr_X)
    ax.add_artist(arr_Y)
    # artist_list.append(ax.add_artist(arr_X))
    # artist_list.append(ax.add_artist(arr_Y))

    # draw square at t0
    square_kw = dict(linewidth=2, edgecolor='black', facecolor='red', fill=False)
    # NOTE: rotation angle is in degrees, not radian
    square = patches.Rectangle(sq_center(t0)+center_to_corner(t0), edge, edge, angle=(w_spin*t0)/np.pi*180, **square_kw)
    ax.add_artist(square)
    # artist_list.append(ax.add_artist(square))

    # add text
    text_kw = dict(fontsize=14, transform=ax.transAxes)
    ax.text(0.1, 0.9, 'In $xy$ system', text_kw)
    # artist_list.append(textbox)

    # plt.show()
    # fig.savefig(dir_path + '/rot_ref_frame.svg')
    # return artist_list

anim = animation.FuncAnimation(fig, animate, init_func=None,
        frames=np.linspace(0, 2*np.pi, 300), interval=20, blit=False)
plt.show()

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
# anim.save(dir_path + '/rot_ref_frame.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
# anim.save(dir_path + '/rot_ref_frame.gif', writer='imagemagick', fps=30)