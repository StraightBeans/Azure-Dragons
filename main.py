import pygame
from os.path import join #cross OS path compatability

# pygame setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("AzureRPG")
running = True

#IMPORTS#

##player/old_man
player_surf  = pygame.image.load(join("sprites", "old_man", ".")).convert_alpha() #SPECIFY OLD MAN SPRITE PATH
player_rect = player_surf.get_frect(center = (100,450))
player_direction = pygame.math.Vector2()
player_velocity = 10

while running:
    clock.tick(60)
    #EVENT LOOP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #RENDERING
    screen.fill("blue") #Background

    ##PLAYER  MOVEMENT
    #if player_rect.right > WINDOW_WIDTH, teleport the player to the scene to the right (same with other directions)
    screen.blit(player_surf, player_rect) #Player

    pygame.display.update()


pygame.quit()
