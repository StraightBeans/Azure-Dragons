from settings import *
from player import Player

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

        #SPRITES#
        self.player = Player((100,300), self.all_sprites)

    def run(self):
        while self.running:
            delta_time = self.clock.tick() / 1000 #Makes player movement consistent across varying fps without capping fps

            #EVENT LOOP#
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            #UPDATE#
            self.all_sprites.update(delta_time)

            #RENDERING#
            self.screen.fill("black")
            self.all_sprites.draw(self.screen)
            pygame.display.update()
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()