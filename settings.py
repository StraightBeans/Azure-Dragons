import pygame
from pathlib import Path

WINDOW_WIDTH, WINDOW_HEIGHT = 800,600
TILE_SIZE = 32

PLAYER_DATA = {
    "Old Man": {"health": 150}, #This will be the old man that fights the cats, made 2 old men to give them different moves so ex. he won't use Custody Papers against a cat
    "Old Man, the Revenger": {"health": 151}, #planning on having him survive on 1 hp on that final battle with the former missus
}

#All entities that can appear in battle, gave the some Elden Ring titles for fun feel free to change things around
ENEMY_DATA = {
    "Martha, the Progenitor": {"health": 50},
    "Ophelia": {"health": 50},
    "Betsy": {"health": 50},
    "Temperance, the Tamed": {"health": 50},
    "Kitty, Blade of Edna": {"health": 100},
    "Edna, the Ex-Wife": {"health": 150},
}

#PHASE1 OLD MAN
PLAYER_ATTACK_DATA = {
    #OLD MAN
    "Pspspsps~~": {"damage": 30},
    "Feed": {"damage": 40},
    "Brush": {"damage": 30},
    "Pet": {"damage": 30},
}

#All cat attacks
CAT_ATTACK_DATA = {
    #CAT
    "uses Scratch": {"damage": 10},
    "Purrs at You": {"damage": 20},
    "Brings a... Rat?": {"damage": 35},
    "Chews on your clothes": {"damage": 20},
}
OLDMAN_STAGETWO_LIST = {
    "Cane": {"damage": 500},
    "Walker": {"damage": 1000}

}

grandma_attack_list = {
    #OLD LADY
    "Cookies": {"damage": 500},
    "Custody Papers": {"damage": 1000}

}