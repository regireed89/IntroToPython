'''get the neighbors'''

import os
import random
import sys


class Node(object):

    def __init__(self, value, identifier):
        self.identifier = identifier
        self.value = value

    def print_info():
        print self.value
        print self.identifier


class Graph(object):
    def __init__(self, dims):
        self.nodes = {}dictionary of nodes
        for i in range(0, dims[0]):
            for j in range(0, dims[1]):
                nodekey = str(i, ",", j)
                node = Node(nodekey, len(self.nodes))
                self.nodes[nodekey] = node

def test_nodes():
    test the nodes
    graph = Graph([3, 3])
    node = get_node(2, graph)
    node.print_info()
    neighbors = get_neighbors(node, graph)
    for nod in neighbors:
        nod.print_info()


if __name__ == '__main__':
    test_nodes()
