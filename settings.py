import pygame
from os.path import join
from os import walk

WINDOW_WIDTH, WINDOW_HEIGHT = 800,600
TILE_SIZE = 32

PLAYER_DATA = {
    0: "Old Man": {"healh: 150"}, #This will be the old man that fights the cats, made 2 old men to give them different moves so ex. he won't use Custody Papers against a cat
    1: "Old Man, the Revenger": {"health": 151}, #planning on having him survive on 1 hp on that final battle with the former missus
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

#All possible attacks
ATTACK_DATA = {
    #CAT
    "Scratch": {"damage": 10},
    "Purr": {"damage": 20},
    #OLD MAN
    "Pspspsps": {"damage": 30},
    "Feed": {"damage": 40},
    "Brush": {"damage": 30},

    ##BOSSES##
    #OLD MAN, the Revenger

    #OLD LADY
    "Custody Papers": {"damage": 1000}
}