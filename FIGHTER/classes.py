import pygame
class game_entity:
    def __init__(self, x=0, y=0, vx=0, vy=0, width=10, height=10, colour=(255, 255, 255), attack_points=0, health_points=100.0):
        # PHYSICS
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

        # SCREEN
        self.w = width
        self.h = height
        self.col = colour

        # GAME
        self.ap = attack_points
        self.hp = health_points

    def update(self, delta_t):
        self.x += self.vx*delta_t
        self.y += self.vy*delta_t
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.col, pygame.Rect( round(self.x), round(self.y), self.w, self.h))