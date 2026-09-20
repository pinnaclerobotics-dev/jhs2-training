# --------------------
# IMPORTS
# --------------------
import os
import pygame
from paths import AUDIO_DIR


# --------------------
# CONSTANTS
# --------------------
MUSIC_FOLDER = "Juhani Junkala [Chiptune Adventures] OGG"
MUSIC_FILE = "Juhani Junkala [Chiptune Adventures] 1. Stage 1.ogg"
MUSIC_PATH = os.path.join(AUDIO_DIR, "bg_music", MUSIC_FOLDER, MUSIC_FILE)
MUSIC_VOLUME = 0.5  # from 0.0 (silent) to 1.0 (full volume)


# --------------------
# MUSIC
# --------------------
def play_background_music():
    """Loads the background music and plays it over and over."""
    pygame.mixer.music.load(MUSIC_PATH)
    pygame.mixer.music.set_volume(MUSIC_VOLUME)
    pygame.mixer.music.play(-1)  # -1 means loop forever
