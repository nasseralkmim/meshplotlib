"""plot elements with nodes coordinates and connectivity"""
from line2d import line2d


def elements2d(xyz, conn, ax):
    """plot elements lines"""
    for ele_nodes in conn:
        for node in ele_nodes[:-1]:
            line2d(xyz[node:node+2, 0],
                   xyz[node:node+2, 1], ax)

        # close element cycle from the last node [-1] to the first [0]
        line2d([xyz[ele_nodes[-1], 0], xyz[ele_nodes[0], 0]],
               [xyz[ele_nodes[-1], 1], xyz[ele_nodes[0], 1]], ax)
