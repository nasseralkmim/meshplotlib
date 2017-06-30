"""plot nodes label in 2d plot"""


def nodes2dlabel(xyz, ax, specific_nodes, **kwargs):
    """plot 2d nodes from xyz array in ax
    
    Args:
        xyz (narray): nodes coordinates
        ax : matplotlib axes object
        specific_nodes (boolean or list): if boolean plot all nodes
          labels, if a list plot olnly labels for nodes in the list
    """
    if specific_nodes is True:
        for i, [x, y] in enumerate(xyz):
            ax.annotate(i, (x, y))
    else:
        for n in specific_nodes:
            ax.annotate(n, (xyz[n, 0], xyz[n, 1]))
