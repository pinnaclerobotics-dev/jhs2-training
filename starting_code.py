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