from logging import setLogRecordFactory
import re
import pygame

from board import *
from assets import *
# circular imports make me want to FUCKING DIEEEEEEEEEEEEEEEEE

TILESIZE: int = 62
BORDERSIZE: int = 50
EDGESIZE: int = 10

class Chess_game:
    def __init__(self) -> None:
        self.white: Player = Player("white")
        self.black: Player = Player("black")
        self.board: Board = Board(self.black, self.white)

        pygame.init()
        self.screen: pygame.Surface = pygame.display.set_mode(
            (TILESIZE * 8 + BORDERSIZE * 2, TILESIZE * 8 + BORDERSIZE * 2))
        self.assets: dict[type, dict[Player, pygame.Surface]] = load_assets(self.white, self.black)
        self.font: dict[str, list[pygame.Surface]] = load_font()

        self.selected: tuple[Optional[int], Optional[int]] = (None, None)
        self.has_selected: bool = False
        self.target: tuple[Optional[int], Optional[int]] = (None, None)

    def __render(self) -> None:
        self.screen.fill(BACKGROUND_COLOR)
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect((BORDERSIZE - EDGESIZE, BORDERSIZE - EDGESIZE), 
                                                             (self.screen.get_size()[0] - BORDERSIZE * 2 + EDGESIZE * 2, 
                                                              self.screen.get_size()[1] - BORDERSIZE * 2 + EDGESIZE * 2)))

        if self.has_selected:
            if self.target[0] != None:
                pygame.draw.rect(self.screen, (0, 0, 255), pygame.Rect(
                    (BORDERSIZE - EDGESIZE ,BORDERSIZE + TILESIZE * self.target[0]), 
                    (self.screen.get_size()[0] - BORDERSIZE * 2 + EDGESIZE * 2, TILESIZE)))
            if self.target[1] != None:
                pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(
                    (BORDERSIZE + TILESIZE * self.target[1], BORDERSIZE - EDGESIZE), 
                    (TILESIZE, self.screen.get_size()[1] - BORDERSIZE * 2 + EDGESIZE * 2)))

        highlighted: list[Piece.Pos] = []

        if self.selected[0] != None and self.selected[1] != None:
            if self.board[self.selected[0]][self.selected[1]] != None:
                highlighted = self.board[self.selected[0]][self.selected[1]].get_moves(self.board)

        for i, row in enumerate(self.board):
            for j, square in enumerate(row):

                color: ccolor = WHITE_SQUARE if (i + j) % 2 == 0 else BLACK_SQUARE
                rect: pygame.Rect = pygame.Rect((BORDERSIZE + j * TILESIZE, BORDERSIZE + i * TILESIZE), (TILESIZE, TILESIZE))

                pygame.draw.rect(self.screen, color, rect)

                overlay: pygame.Surface = pygame.Surface(rect.size)
                overlay.set_alpha(75)
                if (i, j) in highlighted:
                    overlay.fill((255, 0, 0))
                    self.screen.blit(overlay, rect)
                elif (i, j) == self.selected:
                    overlay.fill((0, 100, 255))
                    self.screen.blit(overlay, rect)
                if (i, j) == self.target and self.has_selected:
                    overlay.fill((0, 255, 100))
                    self.screen.blit(overlay, rect)

                if square is None:
                    continue

                surface: pygame.Surface = self.assets[type(square)][square.player]
                self.screen.blit(surface, surface.get_rect(center=rect.center))

        for i in range(len(self.board)):
            key: str = f"{'s' if i == self.selected[0] else ''}n"
            self.screen.blit(self.font[key][i], self.font[key][i].get_rect(topleft=(0, BORDERSIZE + i * TILESIZE)))
        for i in range(len(self.board)):
            key: str = f"{'s' if i == self.selected[1] else ''}t"
            self.screen.blit(self.font[key][i], self.font[key][i].get_rect(topleft=(BORDERSIZE + i * TILESIZE, 0)))

        pygame.display.flip()

    def __handle_press(self, key: int):
        move: tuple[Optional[int], Optional[int]] = (None, None)
        if key == pygame.K_a:
            move = (None, 0)
        elif key == pygame.K_b:
            move = (None, 1)
        elif key == pygame.K_c:
            move = (None, 2)
        elif key == pygame.K_d:
            move = (None, 3)
        elif key == pygame.K_e:
            move = (None, 4)
        elif key == pygame.K_f:
            move = (None, 5)
        elif key == pygame.K_g:
            move = (None, 6)
        elif key == pygame.K_h:
            move = (None, 7)

        elif key == pygame.K_8:
            move = (0, None)
        elif key == pygame.K_7:
            move = (1, None)
        elif key == pygame.K_6:
            move = (2, None)
        elif key == pygame.K_5:
            move = (3, None)
        elif key == pygame.K_4:
            move = (4, None)
        elif key == pygame.K_3:
            move = (5, None)
        elif key == pygame.K_2:
            move = (6, None)
        elif key == pygame.K_1:
            move = (7, None)

        elif key == pygame.K_SPACE:
            self.has_selected = not self.has_selected
        
        if not self.has_selected:
            self.selected = (
                move[0] if move[0] != None else self.selected[0], 
                move[1] if move[1] != None else self.selected[1]
            )
        else:
            self.target = (
                move[0] if move[0] != None else self.target[0], 
                move[1] if move[1] != None else self.target[1]
            )

    def __event_handler(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                self.__handle_press(event.key)
        return False

    def run(self) -> str:
        while True:
            if self.__event_handler():
                break
            self.__render()
        return ""

if __name__ == "__main__":
    history: str = Chess_game().run()
    if input("Save history?\n").lower() in ("y", "yes"):
        raise NotImplementedError
