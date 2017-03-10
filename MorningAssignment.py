'''morning-gist'''
import random


class Player(object):
    '''da player'''

    def __init__(self, cardtotal):
        self.cardtotal = cardtotal


Bob = Player(0)
Jim = Player(0)
Dembois = [Bob, Jim]


def hightotal(mylist):
    '''gets player with highest card total'''

    for play in mylist:
        for i in range(5):
            i = random.choice([5, 10])
            play.cardtotal += i
            if play.cardtotal > play.cardtotal:
                return play, play.cardtotal


if __name__ == '__main__':
    hightotal(Dembois)
