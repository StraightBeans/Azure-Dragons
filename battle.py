from settings import *
import random

class Fighter():
    def __init__(self, name, health, sprite):
        self.name = name
        self.health = health
        self.sprite = sprite

class RhombusButton:
    def __init__(self, center_position, text, key):
        self.center = center_position
        self.text = text
        self.key = key
        self.selected = False

        self.color = pygame.Color("gray50")
        self.font = pygame.font.SysFont(None, 24)

        #POINTS
        x, y = self.center
        size = 60
        self.points = [
            (x, y - size),
            (x + size, y),
            (x, y + size),
            (x - size, y),
        ]

    def draw(self, surface):
        pygame.draw.polygon(surface, self.color, self.points)
        
        #TEXT
        text_surf = self.font.render(self.text, True, "white")
        text_rect = text_surf.get_frect(center=self.center)
        surface.blit(text_surf, text_rect)

class Battle:
    def __init__(self, enemy_name, game):
        self.game = game
        self.screen = pygame.display.get_surface()
        self.running = True
        self.enemy_name = enemy_name

        #SPRITES
        self.player_sprite = pygame.image.load(Path("sprites") / "old_man" / "idle" / "idle0.png").convert_alpha()
        self.player_sprite = pygame.transform.scale(self.player_sprite, (self.player_sprite.get_width() * 3, self.player_sprite.get_height() * 3))

        #IMPORT ENEMY SPRITE
        safe_name = enemy_name.replace(",", "").replace(" ", "") + ".png"
        sprite_path = Path("sprites") / safe_name
        try:
            self.enemy_sprite = pygame.image.load(sprite_path).convert_alpha()
            self.enemy_sprite = pygame.transform.scale(self.enemy_sprite, (self.enemy_sprite.get_width() * 3, self.enemy_sprite.get_height() * 3))
        except:
            self.enemy_sprite = pygame.Surface(50, 50)
            self.enemy_sprite.fill("red")
        
        self.background = pygame.image.load(Path("sprites") / "battlebackground.png")

        #FIGHTERS
        self.player = Fighter("Old Man", PLAYER_DATA["Old Man"]["health"], self.player_sprite)
        self.enemy = Fighter(enemy_name, ENEMY_DATA[enemy_name]["health"], self.enemy_sprite)
        #TURN
        self.is_player_turn:bool = True
        self.attack = None
        self.delay:int = 0

        #ATTACK VISUALS + MOVES
        if enemy_name != "Edna, the Ex-Wife":
            self.attack_buttons = [
                RhombusButton((400, 225), "Pspspsps~~", pygame.K_UP),
                RhombusButton((400, 375), "Feed", pygame.K_DOWN),
                RhombusButton((325, 300), "Brush", pygame.K_LEFT),
                RhombusButton((475, 300), "Pet", pygame.K_RIGHT)
            ]
        else:
             self.attack_buttons = [
                RhombusButton((400, 225), "Custody\nPapers", pygame.K_UP),
                RhombusButton((400, 375), "Photos of\nthe Grandkids", pygame.K_DOWN),
                RhombusButton((325, 300), "Aura Farm", pygame.K_LEFT),
                RhombusButton((475, 300), "...I forgot", pygame.K_RIGHT)
            ]           

        #TEXTBOX
        self.text = ""
        self.text_timer = 0

    def update(self, delta_time):
        #ACTION DELAY
        self.delay -= delta_time
        if self.delay >0:
            return

        if self.is_player_turn:
            self.player_turn()
        else:
            self.enemy_turn()

        #RESET TEXT
        if self.text_timer > 0:
            self.text_timer -= delta_time
            if self.text_timer <= 0:
                self.text = ""
    
    def player_turn(self):
        attack_key = pygame.key.get_just_pressed()
        
        if self.attack is None:
            for button in self.attack_buttons:
                if attack_key[button.key]:
                    self.attack = button.text
                    self.delay = 0.5
                    return
        else:
            if self.delay > 0:
                return
        
        if self.attack:
            #APPLY DAMAGE TO ENEMY + MESSAGE
            damage = PLAYER_ATTACK_DATA[self.attack]["damage"]
            self.enemy.health -= damage
            self.text = f"{self.player.name} used {self.attack}! {self.enemy.name} took {damage} damage!"
            self.text_timer = 2.5


            #END BATTLE / SWITCH TURNS make sure to add a game over for winning against old lady            
            if self.enemy.health <= 0:
                print(f"{self.enemy.name} has fled.")
                self.game.exit_battle()
            else:
                self.is_player_turn = False

            #RESET FOR NEXT TURN
            self.attack = None
            self.delay = 2


    def enemy_turn(self):
        if self.enemy_name != "Edna, the Ex-Wife":
            attack = random.choice(list(CAT_ATTACK_DATA.keys()))
            damage = CAT_ATTACK_DATA[attack]["damage"]
        else:
            attack = random.choice(list(OLDLADY_ATTACK_DATA.keys()))
            damage = OLDLADY_ATTACK_DATA[attack]["damage"]

        #APPLY DAMAGE TO PLAYER + MESSAGE
        self.player.health -= damage
        self.text = f"{self.enemy.name} {attack}! {self.player.name} took {damage} damage!"
        self.text_timer = 2.5

        #END BATTLE / SWITCH TURNS
        if self.player.health <= 0:
            self.game_over()
        else:
            self.is_player_turn = True

    def game_over(self):
        font = pygame.font.SysFont(None, 64)
        text = font.render("Game Over", True, "white")
        text_rect = text.get_frect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))

        self.screen.fill("black")
        self.screen.blit(text, text_rect)
        pygame.display.update()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                    waiting = False

        pygame.quit()

    def render(self, screen):
        screen.blit(self.background, (0,0))

        screen.blit(self.player_sprite, (20, 280))  
        screen.blit(self.enemy_sprite, (650, 440))

        if self.is_player_turn and self.delay <=0:
            for button in self.attack_buttons:
                button.draw(screen)

        #TEXTBOX
        if self.text:
            font = pygame.font.SysFont(None, 32)
            text_surf = font.render(self.text, True, "white")
            text_rect = text_surf.get_frect(center=(self.screen.get_width() // 2, 50))

            pygame.draw.rect(screen, "black", text_rect.inflate(20, 20))
            pygame.draw.rect(screen, "white", text_rect.inflate(20, 20), 2)

            screen.blit(text_surf, text_rect) 