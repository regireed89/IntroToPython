'''morning-gist'''
import random


class Player(object):
    '''da player'''

    def __init__(self, cardtotal):
        self.cardtotal = cardtotal


__player1__ = Player(0)
__player2__ = Player(0)
__Dembois__ = [__player1__, __player2__]


def hightotal(mylist):
    '''gets player with highest card total'''

    for play in mylist:
        for i in range(5):
            i = random.choice([5, 10])
            play.cardtotal += i
            if play.cardtotal > play.cardtotal:
                return play, play.cardtotal


if __name__ == '__main__':
    hightotal(__Dembois__)
