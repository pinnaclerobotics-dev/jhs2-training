# --------------------
# IMPORTS
# --------------------
import random
import pygame
from drawn_sprites import make_stump, make_log


# --------------------
# CONSTANTS
# --------------------
SKY_TOP = (90, 170, 235)        # sky color at the top
SKY_BOTTOM = (200, 235, 255)    # sky color near the horizon
SUN_COLOR = (255, 225, 90)
CLOUD_COLOR = (255, 255, 255)
HILL_COLORS = [(110, 170, 120), (80, 150, 95)]  # far hill, near hill
GRASS_COLOR = (70, 170, 70)
GRASS_BLADE_COLOR = (50, 140, 55)
DIRT_COLOR = (120, 85, 55)
DIRT_DARK_COLOR = (95, 65, 42)
GROUND_HEIGHT = 130             # how tall the land is from the bottom of the window
GRASS_HEIGHT = 30               # thickness of the green strip on top of the land


# --------------------
# DRAWING HELPERS
# --------------------
def draw_sky(surface, width, height):
    """Draws a vertical gradient from SKY_TOP to SKY_BOTTOM."""
    for y in range(height):
        t = y / height
        color = tuple(int(a + (b - a) * t) for a, b in zip(SKY_TOP, SKY_BOTTOM))
        pygame.draw.line(surface, color, (0, y), (width, y))


def draw_cloud(surface, x, y, scale=1.0):
    """Draws a fluffy cloud from overlapping circles."""
    for dx, dy, r in [(0, 0, 30), (35, -15, 38), (75, 0, 32), (35, 8, 30)]:
        pygame.draw.circle(surface, CLOUD_COLOR,
                           (int(x + dx * scale), int(y + dy * scale)), int(r * scale))


def draw_hill(surface, center_x, base_y, hill_width, hill_height, color):
    pygame.draw.ellipse(surface, color,
                        (center_x - hill_width // 2, base_y - hill_height,
                         hill_width, hill_height * 2))


# --------------------
# BACKGROUND
# --------------------
class Background:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.ground_y = height - GROUND_HEIGHT  # y where the land begins
        # everything is drawn once onto one surface, then reused every frame
        # 24-bit means no alpha channel, so the window never ends up see-through (black on macOS)
        self.surface = pygame.Surface((width, height), 0, 24)
        self._build()

    def _build(self):
        rng = random.Random(7)  # fixed seed, so the scenery looks the same every run
        surface = self.surface

        draw_sky(surface, self.width, self.height)
        pygame.draw.circle(surface, SUN_COLOR, (self.width - 160, 120), 55)

        for x, y, scale in [(150, 110, 1.2), (520, 70, 0.9), (860, 150, 1.1), (1000, 50, 0.8)]:
            draw_cloud(surface, x, y, scale)

        # hills sit behind the land, far one first
        for i, color in enumerate(HILL_COLORS):
            for cx in range(-100 + i * 250, self.width + 200, 600):
                draw_hill(surface, cx, self.ground_y + 10, 520 - i * 80, 150 - i * 40, color)

        # land: dirt with a grass strip on top
        pygame.draw.rect(surface, DIRT_COLOR,
                         (0, self.ground_y, self.width, GROUND_HEIGHT))
        for _ in range(60):  # dark dirt specks
            x = rng.randrange(self.width)
            y = rng.randrange(self.ground_y + GRASS_HEIGHT + 5, self.height - 5)
            pygame.draw.ellipse(surface, DIRT_DARK_COLOR, (x, y, 14, 7))
        pygame.draw.rect(surface, GRASS_COLOR,
                         (0, self.ground_y, self.width, GRASS_HEIGHT))
        for x in range(0, self.width, 12):  # grass blades poking above the strip
            h = rng.randint(6, 14)
            pygame.draw.polygon(surface, GRASS_COLOR,
                                [(x, self.ground_y), (x + 5, self.ground_y - h), (x + 10, self.ground_y)])
        for _ in range(120):  # darker blades on the strip for texture
            x = rng.randrange(self.width)
            y = rng.randrange(self.ground_y + 4, self.ground_y + GRASS_HEIGHT - 4)
            pygame.draw.line(surface, GRASS_BLADE_COLOR, (x, y), (x + 2, y - 7), 2)

        # supporting sprites drawn in code
        trunk = make_stump()
        log = make_log()
        for image, x in [(trunk, 90), (log, 330), (trunk, 760), (log, 1010), (trunk, 1200)]:
            surface.blit(image, image.get_rect(midbottom=(x, self.ground_y + GRASS_HEIGHT + 10)))

    def draw(self, surface):
        surface.blit(self.surface, (0, 0))
