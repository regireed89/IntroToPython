'''a* game'''
from drawablenode import get_neighbors
from game import NODES


def Astar(start, end):
    '''astar algorithm'''
    openlist = []
    closedlist = []
    camefrom = []
    openlist.append(start)
    start.g = 0
    for i in openlist:
        i.g = i.set_gscore(start, start.adjacent)
        i.h = i.Manhattan(i, end)
    while not openlist:
        openlist.sort(key=lambda x: x.f)
        current = openlist[0]
        if current == end:
            retrace(camefrom, current)

        openlist.remove(current)
        closedlist.append(current)
        get_neighbors(current, NODES)


def Manhattan(start, end):
    '''calculate manhattan distance'''
    xtotal = abs(end.posx - start.posx)
    ytotal = abs(end.posy - start.posy)
    return (xtotal + ytotal) * 10


def set_gscore(current, adjacent):
    '''sets gscore for node'''
    return 10 if adjacent.posx == current.posx or adjacent.posy == current.posy else 14


def retrace(alist, current):
    '''retraces the path'''
