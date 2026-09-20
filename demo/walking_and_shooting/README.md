# Walking and Shooting Demo

A beginner demo built with pygame-ce.

| Key         | Action      |
| ----------- | ----------- |
| Left arrow  | Walk left   |
| Right arrow | Walk right  |
| Enter       | Shoot water |
| Space       | Shoot fire  |

## Run

```
pip install -r requirements.txt
python main.py
```

## Extra challenges

1. **Attack sound effects** - add a sound effect for each attack: one for the water ball and one for the fire ball. Play it at the moment the projectile is fired.
2. **Physical controls** - edit the code to use hardware instead of the keyboard, with the `pynnacle-nexus` package:
   - One physical button dedicated to each attack (one for the water ball, one for the fire ball).
   - The joystick moves the character left and right.

## Files

- `main.py` - the game loop: window, key presses and drawing.
- `sprites.py` - the character (walking animation, flipping) and the projectiles.
- `drawn_sprites.py` - water, fire, stump and log sprites drawn with `pygame.draw`.
- `scenery.py` - sky, hills, land and grass.
- `audio.py` - looping background music (Juhani Junkala, Chiptune Adventures 1).
- `paths.py` - locations of the shared `assets/` folder at the repo root.
