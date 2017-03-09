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

    def __init__(self,nodes):
        self.nodes = nodes

    def GetNeighbors(node, graph):
        
        return list

    def MakeNodes():
         for i in range(0,25):
            node = Node(i*i,i)
            nodes.append(node)
    graph = Graph(nodes)
    gotnode = graph.GetNeighbors(10)
    gotnode.print_info() 
    
      

    
        
def GetNode(node, graph):
    

A = Node(1, "A")
B = Node(2, "B")
C = Node(3, "C")
D = Node(4, "D")

mymap = [A,B,C,D]
print A.print_info()