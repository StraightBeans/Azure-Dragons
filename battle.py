from settings import *
import random

class Fighter():
    def __init__(self, name, health, sprite):
        self.name = name
        self.health = health
        self.sprite = sprite

class Battle:
    def __init__(self, player_name, enemy_name, game):
        self.game = game
        self.screen = pygame.display.get_surface()
        self.running = True
        self.player_sprite = pygame.image.load(Path("sprites") / "old_man" / "idle" / "idle0.png").convert_alpha()
        self.enemy_sprite = pygame.Surface((50, 50))  # Placeholder square
        self.enemy_sprite.fill("red")

        #FIGHTERS
        self.player = Fighter(player_name, PLAYER_DATA[player_name]["health"], self.player_sprite)
        self.enemy = Fighter(enemy_name, ENEMY_DATA[enemy_name]["health"], self.enemy_sprite)
        #TURN
        self.is_player_turn:bool = True
        self.attack = None
        self.delay:int = 0
# ADD A SPRITE IMPORT FOR ENEMY + RESIZE OLD MAN


    def import_assets(self):
        self.background = self.screen.fill("black")

    def update(self, delta_time):
        #add a small delay before swapping turns
        self.delay -= delta_time
        if self.delay >0:
            return

        if self.is_player_turn == True:
            self.player_turn()
        else:
            self.enemy_turn()
    
    def player_turn(self):
        #ALL ATTACKS, MUST BE THE SAME AS IN SETTINGS.PY
        attack_key = pygame.key.get_just_pressed()
        if attack_key[pygame.K_UP]:
            self.attack = "Pspspsps~~"
        elif attack_key[pygame.K_DOWN]:
            self.attack = "Feed"
        elif attack_key[pygame.K_LEFT]:
            self.attack = "Brush"
        elif attack_key[pygame.K_RIGHT]:
            self.attack = "Pet"
        
        if self.attack:
            damage = PLAYER_ATTACK_DATA[self.attack]["damage"]
            self.enemy.health -= damage
            print(f"{self.player.name} used {self.attack}! {self.enemy.name} took {damage} damage!")
            self.attack = None
            self.delay = 1
            
            if self.enemy.health <= 0:
                print(f"{self.enemy.name} has fled.")
                self.game.exit_battle()
            else:
                self.is_player_turn = False

    def enemy_turn(self):
        attack = random.choice(list(CAT_ATTACK_DATA.keys()))
        damage = CAT_ATTACK_DATA[attack]["damage"]

        self.player.health -= damage
        print(f"{self.enemy.name} {attack}! {self.player.name} took {damage} damage!")

        if self.player.health <= 0:
            print(f"{self.player.name} has been felled.")
            self.game.exit_battle()
        else:
            self.is_player_turn = True

    def render(self, screen):
        screen.fill("black")  # Clear the screen

        # Draw the player sprite (image)
        screen.blit(self.player_sprite, (100, 300))  

        # Draw the enemy as a red square (placeholder)
        pygame.draw.rect(screen, "red", pygame.Rect(500, 300, 50, 50)) 
        