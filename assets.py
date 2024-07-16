from player import Player
from PIL import Image
import PIL.ImageOps
# from main import TILESIZE
IMAGE_SIZE: int = 60

import pygame

ccolor = tuple[int, int, int]
WHITE_SQUARE: ccolor = (245, 243, 219)
BLACK_SQUARE: ccolor = (80, 80, 60)
HIGHLIGHTED_SQUARE: ccolor = (255, 0, 0)
BACKGROUND_COLOR: ccolor = (50, 60, 40)
BACKGROUND_COLOR = BLACK_SQUARE

from pieces import *

def load_assets(white: Player, black: Player) -> dict[type, dict[Player, pygame.Surface]]:
    return {
        Pawn: {
            white: pygame.transform.scale(pygame.image.load("images/white/pawn.png")
                                          .convert_alpha(), (IMAGE_SIZE, IMAGE_SIZE)),
            black: pygame.transform.scale(pygame.image.load("images/black/pawn.png")
                                          .convert_alpha(), (IMAGE_SIZE, IMAGE_SIZE)),
        },
        Rook: {
            white: pygame.transform.scale(pygame.image.load("images/white/rook.png")
                                          .convert_alpha(), (IMAGE_SIZE, IMAGE_SIZE)),
            black: pygame.transform.scale(pygame.image.load("images/black/rook.png")
                                          .convert_alpha(), (IMAGE_SIZE, IMAGE_SIZE)),
        },
        Knight: {
            white: pygame.transform.scale(pygame.image.load("images/white/knight.png")
                                          .convert_alpha(), (IMAGE_SIZE, IMAGE_SIZE)),
            black: pygame.transform.scale(pygame.image.load("images/black/knight.png")
                                          .convert_alpha(), (IMAGE_SIZE, IMAGE_SIZE)),
        },
        Bishop: {
            white: pygame.transform.scale(pygame.image.load("images/white/bishop.png")
                                          .convert_alpha(), (IMAGE_SIZE, IMAGE_SIZE)),
            black: pygame.transform.scale(pygame.image.load("images/black/bishop.png")
                                          .convert_alpha(), (IMAGE_SIZE, IMAGE_SIZE)),
        },
        Queen: {
            white: pygame.transform.scale(pygame.image.load("images/white/queen.png")
                                          .convert_alpha(), (IMAGE_SIZE, IMAGE_SIZE)),
            black: pygame.transform.scale(pygame.image.load("images/black/queen.png")
                                          .convert_alpha(), (IMAGE_SIZE, IMAGE_SIZE)),
        },
        King: {
            white: pygame.transform.scale(pygame.image.load("images/white/king.png")
                                          .convert_alpha(), (IMAGE_SIZE, IMAGE_SIZE)),
            black: pygame.transform.scale(pygame.image.load("images/black/king.png")
                                          .convert_alpha(), (IMAGE_SIZE, IMAGE_SIZE)),
        },
    }

# def invert_image(surf: pygame.Surface) -> pygame.Surface:
#     inv: pygame.Surface = pygame.Surface(surf.get_size())
#     
#     return inv

def load_font() -> dict[str, list[pygame.Surface]]:
    # s for selected
    fonts: dict[str, list[pygame.Surface]] = {
        "t": [pygame.image.load(f"images/text/t_{i}.png").convert_alpha() for i in range(8)],
        "st": [pygame.image.load(f"images/text/st_{i}.png").convert_alpha() for i in range(8)],
        "n": [pygame.image.load(f"images/text/n_{i}.png").convert_alpha() for i in range(8)],
        "sn": [pygame.image.load(f"images/text/sn_{i}.png").convert_alpha() for i in range(8)],
    }
    return fonts
