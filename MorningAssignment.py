'''morning-gist'''
import random


class Player(object):
    '''da player'''

    def __init__(self, name, cardtotal):
        self.name = name
        self.cardtotal = cardtotal


__player1__ = Player("bob", 0)
__player2__ = Player("jim", 0)
__player3__ = Player("carl", 0)
__player4__ = Player("regi", 0)
__Dembois__ = [__player1__, __player2__, __player3__, __player4__]
__current__ = Player("n\a", 0)


def hightotal(mylist):
    '''gets player with highest card total'''

    for play in mylist:
        for i in range(5):
            i = random.choice([5, 10])
            play.cardtotal += i
            if __current__.cardtotal < play.cardtotal:
                __current__.name = play.name
                __current__.cardtotal = play.cardtotal
        print __current__.name, __current__.cardtotal


if __name__ == '__main__':
    hightotal(__Dembois__)
