"""plot mesh from nodal coordinates and connectivity"""
import numpy as np
import matplotlib.pyplot as plt
from nodes2d import nodes2d
from elements2d import elements2d
from nodes2dlabel import nodes2dlabel


def geometry(xyz, conn, ax,
             elements=False,
             nodes=False,
             nodes_label=False):
    """plot geometry"""

    if nodes is True:
        nodes2d(xyz, ax)
    if elements is True:
        elements2d(xyz, conn, ax)
    if nodes_label is True or isinstance(nodes_label, list):
        nodes2dlabel(xyz, ax, nodes_label)


if __name__ is '__main__':
    xyz = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])
    conn = np.array([[0, 1, 2, 3]])
    fig, ax = plt.subplots()
    geometry(xyz, conn, ax, elements=True, nodes_label=True)
    plt.tight_layout()
    plt.show()
