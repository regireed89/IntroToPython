'''get neighbor module'''


class Node(object):
    '''a node'''

    def __init__(self, value, identifier):
        self.value = value
        self.identifier = identifier

    def print_info(self):
        '''print node info'''
        print self.value
        print self.identifier


class Graph(object):
    '''a graph'''

    def __init__(self, x, y):
        self.node = {}
        for i in range(0, x):
            for j in range(0, y):
                nodekey = str([i, ",", j])
                node = Node(nodekey, len(self.node))
                self.node[nodekey] = node

    def __get_node__(self, node, graph):
        '''gets node'''
        if node in graph.node:
            return graph.node[node]


def get_neighbors(node, graph):
    '''gets nodes neighbors'''
    neighbors = []
    right = graph.get_node(node.v )
    if right is None:
        return
    else:
        neighbors.append(right)

    left = graph.get_node(node.nodekey[i - 1, j], graph)
    if left is None:
        return
    else:
        neighbors.append(left)
        top = graph.get_node(node.nodekey[i, j + 1], graph)
    if top is None:
        return
    else:
        neighbors.append(top)
        bottom = graph.get_node(node.nodekey[i, j - 1], graph)
    if bottom is None:
        return
    else:
        neighbors.append(bottom)

    return neighbors



    


def test_nodes():
    '''test the nodes'''
    graph = Graph(3, 3)
    node = graph.get_node(2, graph)
    node.print_info()
    nod = get_neighbors(2, graph)
    nod.print_info()


if __name__ == '__main__':
    test_nodes()
