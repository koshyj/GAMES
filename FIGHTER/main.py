import pygame


class game_entity:
    def __init__(self, x=0, y=0, vx=0, vy=0, ap=0, hp=100.0, group="platform" ):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

        self.ap = ap
        self.hp = hp

        self.group = group

    def update(self, delta_t):
        self.x += self.vx*delta_t
        self.y += self.vy*delta_t
    
    def draw(self, screen):
        pass
    

# GAME FSM
def game_run():

    # Initial Setup
    pygame.display.init()

    # GLOBAL GAME VARIABLES
    # game control
    game_running = 1
    
    # display control
    screen_width = 640
    screen_height = 640

    # objects
    game_entities = []

    # pygame
    screen = pygame.display.set_mode([screen_width, screen_height])
    clock = pygame.time.Clock()

    # Running Game Functions
    while game_running:
        handle()
        update(game_entities, clock)
        draw(game_entities, screen)


# GAME FUNCTIONS
def handle():
    pass

def update(game_entities, clock):
    delta_t = clock.tick(60)
    for entity in game_entities:
        entity.update(delta_t)
    

def draw(game_entities, screen):
    for entity in game_entities:
        entity.draw()


