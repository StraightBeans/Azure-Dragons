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
#player_surf  = pygame.image.load(join("sprites", "old_man", ".")).convert_alpha() #SPECIFY OLD MAN SPRITE PATH
player_surf  = pygame.image.load("IDLE1.png").convert_alpha() 
player_rect = player_surf.get_frect(center = (100,450))
player_direction = pygame.math.Vector2()
player_velocity = 200

while running:
    #EVENT LOOP
    delta_time = clock.tick() / 1000 #Makes player movement consistent across varying fps without capping fps
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #MOVEMENT INPUT
    movekeys = pygame.key.get_pressed()
    player_direction.x = int(movekeys[pygame.K_RIGHT]) - int(movekeys[pygame.K_LEFT])
    player_direction.y = int(movekeys[pygame.K_DOWN]) - int(movekeys[pygame.K_UP])
    player_direction = player_direction.normalize() if player_direction else player_direction
    player_rect.center += player_direction * player_velocity * delta_time

    #RENDERING
    screen.fill("blue") #Background
    screen.blit(player_surf, player_rect) #Player

    ##SCENE TRANSITION
    #if player_rect.right > WINDOW_WIDTH, teleport the player to the scene to the right (same with other directions)

    pygame.display.update()


pygame.quit()
