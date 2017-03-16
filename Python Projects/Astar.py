'''a* game'''
import drawablenode

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


def set_gscore(current, adjacent):
    '''sets gscore for node'''
    return 10 if adjacent.posx == current.posx or adjacent.posy == current.posy else 14
