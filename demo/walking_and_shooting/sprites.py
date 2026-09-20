# --------------------
# IMPORTS
# --------------------
import os
import pygame
from drawn_sprites import make_water_frames, make_fire_frames
from paths import IMAGES_DIR


# --------------------
# CONSTANTS
# --------------------
WALK_DIR = os.path.join(IMAGES_DIR, "main-character", "walking")
WALK_FRAME_COUNT = 4          # walk-0.png ... walk-3.png
WALK_FRAME_TIME = 0.1         # seconds each walking frame is shown
CHARACTER_SPEED = 300         # pixels per second
PROJECTILE_SPEED = 600        # pixels per second
PROJECTILE_FRAME_TIME = 0.08  # seconds each attack picture is shown
PROJECTILE_MAKERS = {         # projectile name -> function that draws its pictures
    "water": make_water_frames,
    "fire": make_fire_frames,
}


# --------------------
# IMAGE HELPERS
# --------------------
def load_image(path):
    """Loads an image with transparency."""
    return pygame.image.load(path).convert_alpha()


def flip_frames(frames):
    """Returns copies of the images flipped horizontally."""
    return [pygame.transform.flip(frame, True, False) for frame in frames]


def load_walk_frames():
    """Loads the walking frames in order (they face right)."""
    return [
        load_image(os.path.join(WALK_DIR, f"walk-{i}.png"))
        for i in range(WALK_FRAME_COUNT)
    ]


# --------------------
# PROJECTILE
# --------------------
class Projectile:
    def __init__(self, name, x, y, direction):
        frames = PROJECTILE_MAKERS[name]()  # the pictures are drawn in code, facing right
        # flip them when shooting left
        self.frames = frames if direction == 1 else flip_frames(frames)
        self.frame_index = 0
        self.timer = 0
        self.rect = self.frames[0].get_rect(center=(x, y))
        self.direction = direction  # 1 = right, -1 = left

    def update(self, dt):
        self.rect.x += self.direction * PROJECTILE_SPEED * dt
        # advance the animation
        self.timer += dt
        if self.timer >= PROJECTILE_FRAME_TIME:
            self.timer -= PROJECTILE_FRAME_TIME
            self.frame_index = (self.frame_index + 1) % len(self.frames)

    def is_offscreen(self, window_width):
        return self.rect.right < 0 or self.rect.left > window_width

    def draw(self, surface):
        surface.blit(self.frames[self.frame_index], self.rect)


# --------------------
# CHARACTER
# --------------------
class Character:
    def __init__(self, x, y, window_width):
        self.frames_right = load_walk_frames()
        self.frames_left = flip_frames(self.frames_right)  # flipped once
        self.facing = 1  # 1 = right, -1 = left
        self.frame_index = 0
        self.timer = 0
        self.window_width = window_width
        self.rect = self.frames_right[0].get_rect(midbottom=(x, y))
        self.x = float(self.rect.x)  # float position for smooth movement

    def _walk(self, direction, dt):
        self.facing = direction
        self.x += direction * CHARACTER_SPEED * dt
        self.x = max(0, min(self.x, self.window_width - self.rect.width))
        self.rect.x = round(self.x)
        # advance the animation
        self.timer += dt
        if self.timer >= WALK_FRAME_TIME:
            self.timer -= WALK_FRAME_TIME
            self.frame_index = (self.frame_index + 1) % WALK_FRAME_COUNT

    def move_left(self, dt):
        self._walk(-1, dt)

    def move_right(self, dt):
        self._walk(1, dt)

    def stand(self):
        self.frame_index = 0
        self.timer = 0

    def shoot(self, name):
        """Returns a new Projectile leaving the front of the character."""
        x = self.rect.right if self.facing == 1 else self.rect.left
        return Projectile(name, x, self.rect.centery, self.facing)

    def draw(self, surface):
        frames = self.frames_right if self.facing == 1 else self.frames_left
        surface.blit(frames[self.frame_index], self.rect)
