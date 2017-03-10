'''get neighbor module'''


class Node(object):
    '''a node'''

    def __init__(self, value, identifier):
        self.value = value
        self.identifier = identifier

    def __print_info(self):
        '''print node info'''
        print self.value
        print self.identifier


class Graph(object):
    '''a graph'''

    def __init__(self, length, width):
        self.node = {}
        for i in range(0, length):
            for j in range(0, width):
                nodekey = str([i, ",", j])
                node = Node(nodekey, len(self.node))
                self.node[nodekey] = node

    def get_node(self, node, graph):
        '''gets node'''
        for node in graph:
            if node == graph.node:
                return graph.node[node]


def test_nodes():
    '''test the nodes'''
    graph = Graph(3, 3)
    node = graph.get_node(2, graph)
    node.print_info()


if __name__ == '__main__':
    test_nodes()
