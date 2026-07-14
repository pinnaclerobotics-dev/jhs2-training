# --------------------
# IMPORTS
# --------------------
import pygame # imports pygame-ce


# --------------------
# CONSTANTS
# --------------------
WINDOW_WIDTH = 1280 # window's width
WINDOW_HEIGHT = 720 # window's height


# --------------------
# INITIALIZATION
# --------------------
pygame.init() # initializes pygame-ce
# creates a display surface and stores it in a variable
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) 


# --------------------
# GAME LOOP
# --------------------
running = True  # initially True and will be set to False if the user quits
while running:
    # Event Loop
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False # set running to False to exit game loop (outer while loop)

# --------------------
# CLEANUP
# --------------------
pygame.quit() # uninitializes pygame-ce modules