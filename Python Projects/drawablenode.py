'''drawablenode'''
import pygame
import math


class DrawableNode(object):
    '''drawable node'''

    def __init__(self, graphpos, ident):
        '''init'''
        # astar vars
        self.posx = graphpos[0]
        self.posy = graphpos[1]
        self.adjacents = []
        self.parent = None
        self._walkable = True
        self._g = 0
        self._h = 0
        self._f = 0

        # drawing vars
        SIZE = 50
        self.width = SIZE
        self.height = SIZE
        self.identification = ident
        self.index = [self.posx, self.posy]
        self.x = (5 + self.width) * self.posx + 5
        self.y = (5 + self.height) * self.posy + 5
        self.pos = (self.width * self.posx, self.height * self.posy)
        self.screenpos = (self.x, self.y)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.surface = pygame.Surface((self.width, self.height))
        self.dirty = False
        self._color = (125, 255, 255)


    def get_neighbors(self, listt):
        '''gets the neighbors of a node'''
        dirs = []
        right = listt[self.identification + 10]
        if right is not None:
            dirs.append(right) 

        top_right = listt[self.identification + 9]
        if top_right is not None:
            dirs.append(top_right)

        top = listt[self.identification - 1]
        if top is not None:
            dirs.append(top)

        top_left = listt[self.identification - 11]
        if top_left is not  None:
            dirs.append(top_left)

        left = listt[self.identification - 10]
        if left is not None:
            dirs.append(left)

        bottom_left = listt[self.identification - 9]
        if bottom_left is not None:
            dirs.append(bottom_left)

        bottom = listt[self.identification + 1]
        if bottom is not None:
            dirs.append(bottom)

        bottom_right = listt[self.identification + 11]
        if bottom_right is not None:
            dirs.append(bottom_right)

        self.adjacents = list(dirs)

        return self.adjacents


    # properties
    @property
    def walkable(self):
        return self._walkable

    @walkable.setter
    def walkable(self, value):
        white = (255, 255, 255)
        red = (255, 0, 0)
        self._walkable = value
        # if it's set to walkable change to white
        # this will mark it as undirty
        if value:
            self.color = (255, 255, 255)
        else:
            self.color = (255, 0, 0)

    @property
    def f(self):
        return self._f

    @property
    def g(self):
        return self._g

    @property
    def h(self):
        return self._h

    @f.setter
    def f(self, value):
        self._f = value

    @g.setter
    def g(self, value):
        self._g = value
        self._f = self._g + self._h

    @h.setter
    def h(self, value):
        self._h = value
        self._f = self._g + self._h

    @property
    def color(self):
        return self._color

    @property
    def start(self):
        return self.start

    @property
    def end(self):
        return self.end

    @color.setter
    # manual setting of colors will mark them dirty so they will stay
    def color(self, value):
        white = (255, 255, 255)
        red = (255, 0, 0)

        if value is red:
            self._color = value
            self.dirty = True
        else:
            self._color = value

        self._color = value

    def info(self):
        print("pos = ", self.pos)
        ids = ""
        for i in self.adjacents:
            ids += " " + str(i.id)
        print("neighbors:", ids)
        print("index: ", self.index)

    def draw(self, screen, font, init=True, text=True):
        # pygame.draw.rect(screen, self._color, self.rect)
        self.surface.fill(self._color)
        screen.blit(self.surface, self.screenpos)
        if self.walkable:
            # create some text to go on the fill

            # info to display

            # render the text

            textf = font.render("F= " + str(self.f), True, (1, 1, 1))
            textg = font.render("G= " + str(self.g) +
                                "H= " + str(self.h), True, (1, 1, 1))

            # set it's position/parent
            textfpos = (self.x, self.y)  # top left
            textgpos = (self.x, self.y + self.height - 10)  # bot left

            # center it

            # draw the square
            if init and text:
                screen.blit(textf, textfpos)
                screen.blit(textg, textgpos)


