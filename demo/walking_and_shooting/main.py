# --------------------
# IMPORTS
# --------------------
import pygame # imports pygame-ce
from sprites import Character # our character, animation and projectile logic
from scenery import Background # sky, land, grass and other decorations
from audio import play_background_music # background music


# --------------------
# CONSTANTS
# --------------------
WINDOW_WIDTH = 1280 # window's width
WINDOW_HEIGHT = 720 # window's height
FPS = 60 # frames per second


# --------------------
# INITIALIZATION
# --------------------
pygame.init() # initializes pygame-ce
# creates a display surface and stores it in a variable
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock() # keeps the game running at a steady speed
background = Background(WINDOW_WIDTH, WINDOW_HEIGHT) # the scenery behind the character
# creates the character at the bottom-center of the window
player = Character(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50, WINDOW_WIDTH)
projectiles = [] # water and fire attacks currently flying
dt = 0 # seconds since the last frame
play_background_music() # starts the background music (loops forever)


# --------------------
# GAME LOOP
# --------------------
running = True  # initially True and will be set to False if the user quits
while running:
    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # set running to False to exit game loop (outer while loop)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                projectiles.append(player.shoot("water")) # enter shoots water
            elif event.key == pygame.K_SPACE:
                projectiles.append(player.shoot("fire")) # space shoots fire

    # Movement (checks which keys are being held down)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move_left(dt) # walk left
    elif keys[pygame.K_RIGHT]:
        player.move_right(dt) # walk right
    else:
        player.stand() # no key pressed, so stand still

    # Update projectiles and remove the ones that left the window
    for projectile in projectiles[:]:
        projectile.update(dt)
        if projectile.is_offscreen(WINDOW_WIDTH):
            projectiles.remove(projectile)

    # Draw
    background.draw(window) # sky, land, grass and decorations
    for projectile in projectiles:
        projectile.draw(window)
    player.draw(window)
    pygame.display.flip() # shows everything we drew

    dt = clock.tick(FPS) / 1000 # limits to FPS and gets seconds since last frame

# --------------------
# CLEANUP
# --------------------
pygame.quit() # uninitializes pygame-ce modules
