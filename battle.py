from settings import *

class Battle:
    def __init__(self, player, enemy, background):
        self.player = PLAYER_DATA
        self.enemy = ENEMY_DATA
        self.screen = pygame.display.get_surface()

    def update(self, delta_time):
        self.screen.fill("white")