# --------------------
# IMPORTS
# --------------------
import os


# --------------------
# CONSTANTS
# --------------------
# this file lives in <repo>/demo/walking_and_shooting/, so the repo root is 2 folders up
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ASSETS_DIR = os.path.join(ROOT_DIR, "assets")   # the assets folder shared by the whole repo
IMAGES_DIR = os.path.join(ASSETS_DIR, "images")
AUDIO_DIR = os.path.join(ASSETS_DIR, "audio")
