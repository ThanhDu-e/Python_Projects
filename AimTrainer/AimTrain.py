import math
import random
import time
import pygame # Basic UI
pygame.init # initialize pygame and basics


WIDTH, HEIGHT = 800, 600 # use to set pygame display size. Number of pixels

WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # initialize display window and display it on screen

pygame.display.set_caption("Aim Trainer") # Sets the name for the window

TARGET_INTERVAL = 400 # time interval between target showing up
TARGET_EVENT = pygame.USEREVENT 

TARGET_PADDING = 30

BG_COLOR = (0, 25, 40) # red, green, blue


# Class to create target to aim at
class Target:
    MAX_SIZE = 30
    GROWTH_RATE = 0.2
    COLOR = "red"
    SECOND_COLOR = "white"

# Target Constructor
# self - refers to the target itself
# x, y - positional to place on the screen
    def __init__(self, x, y):
        self.x = x # x positional value
        self.y = y # y positional value
        self.size = 0 # initial size of the target
        self.grow = True # allows the target to grow until MAX_SIZE is reached
    
    # Update the Target Size
    def update(self):
        # target's size + growth_rate >= MAX_SIZE, make grow boolean False
        if self.size + self.GROWTH_RATE >= self.MAX_SIZE:
            self.grow = False
        
        # if grow is still true, increase the target's size by adding the GROWTH_RATE
        if self.grow:
            self.size += self.GROWTH_RATE
        
        # Shrink the target's size by subtracting the GROWTH_RATE
        else:
            self.size -= self.GROWTH_RATE
    

    # Draws the target onto a window object
    def draw(self, win):

        # draw Target circles: pass the window target is drawn onto, the color of circle, center position, and radius
        # Overlap the circles to create target design
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.size)
        pygame.draw.circle(win, self.SECOND_COLOR, (self.x, self.y), self.size * 0.8)
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.size * 0.6)
        pygame.draw.circle(win, self.SECOND_COLOR, (self.x, self.y), self.size * 0.4)


def draw(win, targets):
    win.fill(BG_COLOR)

    for target in targets:
        target.draw(win)

        pygame.display.update()

# Loops and look for different events that occur
def main(): 

    run = True
    
    # stores all the Target objects and draw them on the screen
    targets = []
    clock = pygame.time.Clock() 
    # sets the TARGET_EVENT to happen every TARGET_INTERVAL
    pygame.time.set_timer(TARGET_EVENT, TARGET_INTERVAL)


    while(run):
        clock.tick(60) # regulates the speed of which the computer runs. 60 fps
        # loop through all events that are occuring
        for event in pygame.event.get():
            # if the event is exit, break the
            if event.type == pygame.QUIT:
                run = False
                break

            # Create new Target object whenever event is triggered and add it to list
            if event.type == TARGET_EVENT:
                x = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                y = random.randint(TARGET_PADDING, HEIGHT - TARGET_PADDING)

                target = Target(x, y)
                targets.append(target)
        
        for target in targets: 
            target.update() # updates all Targets in the list

            if target.size <= 0:
                targets.remove(target) # if a target size is 0 or below, it is removed.


        draw(WIN, targets)

    pygame.quit()

if __name__ == "__main__":
    main()