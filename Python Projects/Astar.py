'''a* game'''


def Astar(start, end):
    '''astar algorithm'''
    openlist = []
    closedlist = []
    openlist.append(start)
    g = []
    g[start] = 0


def MHD(graph, start, end):
    '''calculate manhattan distance'''
    X = abs(graph.start.x - graph.end.x)
    Y = abs(graph.start.y - graph.end.y)
    return print X + Y * 10
