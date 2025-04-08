import pygame
from pathlib import Path

WINDOW_WIDTH, WINDOW_HEIGHT = 800,600
TILE_SIZE = 32

PLAYER_DATA = {
    "Old Man": {"health": 150}, #This will be the old man that fights the cats, made 2 old men to give them different moves so ex. he won't use Custody Papers against a cat
}

#All entities that can appear in battle, gave the some Elden Ring titles for fun feel free to change things around
ENEMY_DATA = {
    "Martha, the Progenitor": {"health": 50},
    "Ophelia": {"health": 50},
    "Temperance, the Tamed": {"health": 50},
    "Kitty, Blade of Edna": {"health": 100},
    "Edna, the Ex-Wife": {"health": 150},
}

PLAYER_ATTACK_DATA = {
    #VS CAT MOVESET
    "Pspspsps~~": {"damage": 30},
    "Feed": {"damage": 40},
    "Brush": {"damage": 30},
    "Pet": {"damage": 30},

    #VS BOSS MOVESET
    "Custody\nPapers": {"damage": 50},
    "Photos of\nthe Grandkids": {"damage": 50},
    "Aura Farm": {"damage": 35},
    "...I forgot": {"damage": 0},
}

CAT_ATTACK_DATA = {
    #CAT
    "uses Scratch": {"damage": 10},
    "Purrs at You": {"damage": 20},
    "Brings a... Rat?": {"damage": 35},
    "Chews on your clothes": {"damage": 20},
}

OLDLADY_ATTACK_DATA = {
    #OLD LADY
    "Bakes Cookies": {"damage": 40},
    "Summons her Cats": {"damage": 35},
    "Sprays Fabuloso on You": {"damage": 35},
    "Hums a forgotten lullaby": {"damage": 40},
}