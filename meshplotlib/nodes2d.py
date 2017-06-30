"""plot nodes in 2d plot"""


def nodes2d(xyz, ax, **kwargs):
    """plot 2d nodes from xyz array in ax
    """
    ax.scatter(xyz[:, 0], xyz[:, 1], marker='s',
               edgecolor='k',
               facecolor='none',
               **kwargs)
