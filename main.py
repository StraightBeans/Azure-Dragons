from settings import *
from player import Player
from sprites import *

class Game:
    def __init__(self):
        #PYGAME SETUP#
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("AzureRPG")
        self.clock = pygame.time.Clock()
        self.running =  True

        #GROUPS#
        self.all_sprites = pygame.sprite.Group() 
        self.collision_sprites = pygame.sprite.Group()
        self.battle_sprites = pygame.sprite.Group()

        #OVERWORLD# ex. everything taking place in the top-down perspective
        ##SPRITES
        ###PLAYER
        self.player = Player((100,300), self.all_sprites, self.collision_sprites, self.battle_sprites)

        ###COLLISIONS
        Collision_Sprite((300,300), (20,60), self.collision_sprites)
 
        ###ENTER BATTLE
        Battle_Sprite((600, 300), (20,20), self.battle_sprites)

        #BATTLE#
        self.battle = None


    def run(self):
        while self.running:
            delta_time = self.clock.tick() / 1000 #Makes player movement consistent across varying fps, so no need to cap fps

            #EVENT LOOP#
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            #UPDATE#
            self.all_sprites.update(delta_time)

            #RENDERING#
            self.screen.fill("black")
            self.all_sprites.draw(self.screen)
            self.collision_sprites.draw(self.screen)
            self.battle_sprites.draw(self.screen)
            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()