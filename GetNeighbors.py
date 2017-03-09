import os
import random
import sys

class Node(object):
    
    letter = ""
    def __init__(self, value, identifier):
        self.identifier = identifier
        self.value = value


class Graph(object):

    def __init__(self,g):
        self.nodes = nodses
    

    def GetNeighbors(node, graph):
        return list;

def makenodes():
    nodes = []
    for i in range(0,25):
        node = Node(i*i,i)
        nodes.append(node)
    graph = Graph(nodes)
    gotnode = graph.GetNeighbors(10)
    gotnode.print_info()    

