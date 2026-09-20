# --------------------
# IMPORTS
# --------------------
import pygame


# --------------------
# CONSTANTS
# --------------------
WATER_SIZE = (64, 40)
FIRE_SIZE = (72, 44)
ANIMATION_FRAMES = 3  # number of slightly different pictures per attack

WATER_LIGHT = (140, 210, 255)
WATER_MID = (60, 160, 250)
WATER_DARK = (25, 100, 210)
WHITE = (255, 255, 255)

FIRE_RED = (220, 50, 20)
FIRE_ORANGE = (255, 140, 20)
FIRE_YELLOW = (255, 225, 70)
FIRE_CORE = (255, 250, 210)

BARK = (125, 85, 50)
BARK_DARK = (90, 58, 34)
WOOD_LIGHT = (200, 155, 100)


# --------------------
# ATTACKS (all of them face right)
# --------------------
def make_water_frame(frame):
    """Draws one picture of the water attack: a blob of water with a droplet trail."""
    surface = pygame.Surface(WATER_SIZE, pygame.SRCALPHA)
    wobble = (frame - 1) * 3  # -3, 0 or 3 pixels, makes the trail wiggle

    # tapered trail behind the blob
    pygame.draw.polygon(surface, WATER_MID, [(46, 7), (10, 20 + wobble), (46, 33)])
    # little droplets that got left behind
    pygame.draw.circle(surface, WATER_MID, (16, 12 - wobble), 4)
    pygame.draw.circle(surface, WATER_MID, (8, 27 + wobble), 3)
    pygame.draw.circle(surface, WATER_LIGHT, (3, 18 - wobble), 2)

    # the main blob, drawn as a dark circle with lighter circles inside it
    pygame.draw.circle(surface, WATER_DARK, (46, 20), 15)
    pygame.draw.circle(surface, WATER_MID, (46, 20), 13)
    pygame.draw.circle(surface, WATER_LIGHT, (48, 22), 8)
    pygame.draw.circle(surface, WHITE, (41, 14), 4)  # shiny highlight
    return surface


def make_fire_frame(frame):
    """Draws one picture of the fire attack: a fireball with a flickering flame tail."""
    surface = pygame.Surface(FIRE_SIZE, pygame.SRCALPHA)
    a = (frame % 3) * 3      # different flame tip heights for each frame,
    b = ((frame + 1) % 3) * 3  # so the fire looks like it is flickering

    def flame(color, shrink):
        """A zigzag flame polygon; a bigger 'shrink' makes a smaller flame."""
        points = [(50, 8 + shrink), (38, 5 + a + shrink), (30, 12 + shrink),
                  (18, 9 + b + shrink), (6 + shrink * 2, 22),
                  (18, 35 - b - shrink), (30, 32 - shrink), (38, 39 - a - shrink),
                  (50, 36 - shrink)]
        pygame.draw.polygon(surface, color, points)

    flame(FIRE_RED, 0)
    flame(FIRE_ORANGE, 4)
    flame(FIRE_YELLOW, 8)

    # the fireball head
    pygame.draw.circle(surface, FIRE_RED, (52, 22), 15)
    pygame.draw.circle(surface, FIRE_ORANGE, (52, 22), 12)
    pygame.draw.circle(surface, FIRE_YELLOW, (53, 22), 8)
    pygame.draw.circle(surface, FIRE_CORE, (54, 22), 4)
    return surface


def make_water_frames():
    return [make_water_frame(i) for i in range(ANIMATION_FRAMES)]


def make_fire_frames():
    return [make_fire_frame(i) for i in range(ANIMATION_FRAMES)]


# --------------------
# SCENERY PROPS
# --------------------
def make_stump():
    """Draws a tree stump."""
    surface = pygame.Surface((60, 50), pygame.SRCALPHA)
    pygame.draw.rect(surface, BARK, (6, 16, 48, 30), border_radius=8)   # trunk
    for x in (16, 28, 40):                                               # bark lines
        pygame.draw.line(surface, BARK_DARK, (x, 24), (x, 42), 2)
    pygame.draw.ellipse(surface, BARK_DARK, (4, 6, 52, 22))              # top edge
    pygame.draw.ellipse(surface, WOOD_LIGHT, (6, 7, 48, 18))             # cut top
    pygame.draw.ellipse(surface, BARK, (16, 11, 28, 10), 2)              # tree rings
    pygame.draw.ellipse(surface, BARK, (24, 14, 12, 4), 2)
    return surface


def make_log():
    """Draws a log lying on its side."""
    surface = pygame.Surface((84, 36), pygame.SRCALPHA)
    pygame.draw.rect(surface, BARK, (8, 6, 72, 26), border_radius=10)   # body
    for y in (12, 19, 26):                                               # bark lines
        pygame.draw.line(surface, BARK_DARK, (24, y), (72, y), 2)
    pygame.draw.ellipse(surface, BARK_DARK, (0, 5, 22, 28))              # cut end
    pygame.draw.ellipse(surface, WOOD_LIGHT, (2, 7, 18, 24))
    pygame.draw.ellipse(surface, BARK, (6, 13, 10, 12), 2)               # tree rings
    return surface
