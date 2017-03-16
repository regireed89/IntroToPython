'''a* game'''


def Astar(start, end):
    '''astar algorithm'''
    openlist = []
    closedlist = []
    openlist.append(start)
    g = []
    g[start] = 0


def Manhattan(start, end):
    '''calculate manhattan distance'''
    xtotal = abs(end.posx - start.posx)
    ytotal = abs(end.posy - start.posy)
    return (xtotal + ytotal) * 10


def get_gval(current, n):
    return 10 if n.posx == current.posx or n.posy == current.posy else 14
