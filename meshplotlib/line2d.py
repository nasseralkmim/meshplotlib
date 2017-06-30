"""plot a line between 2 points"""
from matplotlib.lines import Line2D


def line2d(x, y, ax, **kwargs):
    """plot a 2d line between (x1, y1) and (x2, y2)"""
    line = Line2D(x, y, linewidth=1, color='k', **kwargs)
    ax.add_line(line)
