import pygame
from classes import *

# GLOBAL CONTROL
game_running = 0

# display control
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640
FPS = 60
BACKGROUND_COLOUR = (0, 0, 0)

# GAME OBJECTS
game_entities = [game_entity(100, 100, 20, 15, 20, 20)]
# pygame
screen = pygame.display.set_mode( [SCREEN_WIDTH, SCREEN_HEIGHT] )
clock = pygame.time.Clock()

# physics control
delta_t = 0

    

# GAME FSM
def game_run():
    # Initial Setup
    pygame.init()

    # start game loop
    game_running = 1 
    while game_running:
        # Running Game Functions
        handle()
        draw(game_entities, screen)
        update(game_entities, clock)
        

# GAME FUNCTIONS
def handle():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = 0
            pygame.quit()

def update(game_entities, clock):
    delta_t = clock.tick_busy_loop(FPS)/1000.0
    for entity in game_entities:
        entity.update(delta_t)
    

def draw(game_entities, screen):
    screen.fill(BACKGROUND_COLOUR)
    for entity in game_entities:
        entity.draw(screen)    
    pygame.display.flip()


game_run()

