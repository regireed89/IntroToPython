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

    def get_node(self, node, graph):
        '''gets node'''
        @classmethod
        if node == graph.node:
            return graph.node[node]


def get_neighbors(node, graph):
    '''gets nodes neighbors'''
    neighbors = []
    graph.node[node] = graph.node[node.x] + 1
    if graph.node[node] is None:
        return
    else:
        neighbors.append(graph.node[node])

    graph.node[node] = graph.node[node.y] + 1
    if graph.node[node] is None:
        return
    else:
        return graph.node[node]


def test_nodes():
    '''test the nodes'''
    graph = Graph(3, 3)
    node = graph.get_node(2, graph)
    node.print_info()
    nod = get_neighbors(2, graph)
    nod.print_info()


if __name__ == '__main__':
    test_nodes()
