
#Start by importing pygame and its local files into the environment
import pygame, sys
from pygame.locals import *

#This command initializes the program
pygame.init()

#We need to assign an FPS value to the program. This is the refresh rate,
#or the number of pictures that the program draws per second
FPS = 30
FramePerSec = pygame.time.Clock()

#In Pygame, we set color objects with
#RGB values (tuple format with three values).
#We need to set up color objects in the program
#Blue = (0, 0, 255)
#Red = (255, 0, 0)
#Green = (0, 255, 0)
#Black = (0, 0, 0)
#White = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)

#We now need to set a display, with a caption
screen = pygame.display.set_mode((300, 300))
screen.fill(red)
pygame.display.set_caption("Just playing around in Pygame!")

#We can use the following strings to create
#lines and shapes in the program
#pygame.draw.line(screen, white, (150,130), (130,170))
#pygame.draw.circle(screen, white, (150,130), (130,170))
#pygame.draw.rect(screen, white, (150,130), (130,170))
pygame.draw.line(screen, black, (150,130), (130,170))
pygame.draw.line(screen, black, (150,130), (170,170))
pygame.draw.line(screen, black, (130,170), (170,170))

#Every program will need a game loop to run the game.
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        FramePerSec.tick(FPS)
