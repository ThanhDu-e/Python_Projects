import math
import random
import time
import pygame # Basic UI
pygame.init() # initialize pygame and basics


WIDTH, HEIGHT = 800, 600 # use to set pygame display size. Number of pixels

WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # initialize display window and display it on screen

pygame.display.set_caption("Aim Trainer") # Sets the name for the window

TARGET_INTERVAL = 400 # time interval between target showing up
TARGET_EVENT = pygame.USEREVENT 

TARGET_PADDING = 30

BG_COLOR = (0, 25, 40) # red, green, blue

LIVES = 3

TOP_BAR_HEIGHT = 50

LABEL_FONT = pygame.font.SysFont("comicsans", 24)

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

    def collide(self, x, y):
        dis = math.sqrt((self.x - x)**2 + (self.y - y)**2)
        return dis <= self.size


def draw(win, targets):
    win.fill(BG_COLOR)

    for target in targets:
        target.draw(win)



def format_time(secs):
    milli = math.floor(int(secs*1000 % 1000) / 100)
    second = int(round(secs % 60, 1))
    minute = int(secs // 60)

    return f"{minute:02d}:{second:02d}:{milli}"


def draw_top_bar(win, elapsed_time, targets_pressed, misses):
    pygame.draw.rect(win, "grey", (0,0, WIDTH, TOP_BAR_HEIGHT))
    time_label = LABEL_FONT.render(
        f"Time: {format_time(elapsed_time)}", 1, "black")

    speed = round(targets_pressed / elapsed_time, 1)
    speed_label = LABEL_FONT.render(f"Speed: {speed} t/s", 1, "black")
    
    hits_label = LABEL_FONT.render(f"Hits: {targets_pressed}", 1, "black")

    lives_label = LABEL_FONT.render(f"Lives: {LIVES - misses}", 1, "black")


    win.blit(time_label, (5, 5))
    win.blit(speed_label, (200, 5))
    win.blit(hits_label, (450, 5))
    win.blit(lives_label, (650, 5))


def end_screen(win, elapsed_time, targets_pressed, clicks):
    WIN.fill(BG_COLOR)
    time_label = LABEL_FONT.render(
        f"Time: {format_time(elapsed_time)}", 1, "white")

    speed = round(targets_pressed / elapsed_time, 1)
    speed_label = LABEL_FONT.render(f"Speed: {speed} t/s", 1, "white")
    
    hits_label = LABEL_FONT.render(f"Hits: {targets_pressed}", 1, "white")

    accuracy = round(targets_pressed / clicks * 100, 1)
    accuracy_label = LABEL_FONT.render(f"Accuracy: {accuracy}", 1, "white")

    win.blit(time_label, (get_middle(time_label), 100))
    win.blit(speed_label, (get_middle(speed_label), 200))
    win.blit(hits_label, (get_middle(hits_label), 300))
    win.blit(accuracy_label, (get_middle(accuracy_label), 400))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                quit()

def get_middle(surface):
    return WIDTH/2 - surface.get_width()/2

# Loops and look for different events that occur
def main(): 

    run = True
    
    # stores all the Target objects and draw them on the screen
    targets = []
    clock = pygame.time.Clock() 

    target_pressed = 0 # tracks how many targets clicked
    clicks = 0 # tracks number of clicks
    misses = 0 # tracks number of targets missed
    start_time = time.time() # timer

    # for every TARGET_INTERVAL that elapse, TARGET_EVENT will occur
    pygame.time.set_timer(TARGET_EVENT, TARGET_INTERVAL)


    while(run):
        clock.tick(60) # regulates the speed of which the computer runs. 60 fps
        click = False # Determines if a the mouse is clicked
        mouse_pos = pygame.mouse.get_pos()
        elapsed_time = time.time() - start_time

        # loop through all events that are occuring
        for event in pygame.event.get():
            # if the event is exit, break the
            if event.type == pygame.QUIT:
                run = False
                break

            # Create new Target object whenever TARGET_EVENT is triggered and add it to list
            if event.type == TARGET_EVENT:
                # generate random positional values within the GUI window
                x = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                y = random.randint(TARGET_PADDING + TOP_BAR_HEIGHT, HEIGHT - TARGET_PADDING)
                
                # create new Target object 
                target = Target(x, y)
                targets.append(target)

            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                clicks += 1
        
        for target in targets: 
            target.update() # updates all Targets in the list

            if target.size <= 0:
                targets.remove(target) # if a target size is 0 or below, it is removed.
                # if target hits 0, it is considered a miss
                misses += 1


            # astrick breaks down the tuples into separate elements
            if click and target.collide(*mouse_pos):
                targets.remove(target)
                target_pressed += 1

        if misses >= LIVES:
            end_screen(WIN, elapsed_time, target_pressed, clicks)

        draw(WIN, targets)
        draw_top_bar(WIN, elapsed_time, target_pressed, misses)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()