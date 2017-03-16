# Import a library of functions called 'pygame'
import pygame
import graph as graphs
from graph import Graph
from drawablenode import get_neighbors
import drawablenode
from drawablenode import *
import Astar
from Astar import Manhattan
from Astar import set_gscore
# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PAD = (5, 5)
ROWS = 10
COLS = 10
WIDTH = 50
HEIGHT = 50
SCREEN_WIDTH = COLS * (PAD[0] + WIDTH) + PAD[1]
SCREEN_HEIGHT = ROWS * (PAD[0] + HEIGHT) + PAD[1]
# Set the height and width of the SCREEN

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
search_space = Graph([ROWS, COLS])

NODES = []
for i in range(ROWS):
    for j in range(COLS):
        node = search_space.get_node([i, j])
        NODES.append(DrawableNode(node))

pygame.display.set_caption("Example code for the draw module")

# Loop until the user clicks the close button.
DONE = False
CLOCK = pygame.time.Clock()

pygame.font.init()
font1 = pygame.font.Font(None, 14)
font2 = pygame.font.Font(None, 28)
walls = [NODES[42], NODES[43], NODES[44], NODES[45], NODES[46]]
for i in walls:
    i.color = BLACK
    i.walkable = False
start = NODES[1]
start.color = GREEN
end = NODES[55]
end.color = RED
for i in NODES:
    i.h = Manhattan(i, end)
start.adjacents = get_neighbors(start, search_space)
for a in start.adjacents:
    a.g = set_gscore(start, a)



while not DONE:
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    CLOCK.tick(10)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            DONE = True  # Flag that we are DONE so we exit this loop

    # All drawing code happens after the for loop and but
    # inside the main while DONE==False loop.

    # Clear the SCREEN and set the SCREEN background
    SCREEN.fill(WHITE)
    # Draw a circle
    for i in NODES:
        i.draw(SCREEN, font1)

    # Go ahead and update the SCREEN with what we've drawn.
    # This MUST happen after all the other drawing commands.
    bg = pygame.Surface((SCREEN.get_size()[0] / 3, SCREEN.get_size()[1] / 3))
    bg.fill(BLACK)
    textrect = bg.get_rect()
    pygame.display.flip()


# Be IDLE friendly
pygame.quit()
