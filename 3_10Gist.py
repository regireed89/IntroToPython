'''3_10Gist'''
import random


class Player(object):
    '''da player'''

    def __init__(self, cardtotal):
        self.cardtotal = cardtotal


bob = Player(0)
jim = Player(0)
dembois = [bob, jim]


def HighTotal(list):

    for p in list:
        for t in range(0, 5):
            x += random.choice([5, 10])
            p.cardtotal += x
            if p.cardtotal > p.cardtotal:
                return p, p.cardtotal


HighTotal(dembois)
