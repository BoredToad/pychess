from typing import Self, Optional
from player import *

class Piece:
    t_board = list[list[Optional[Self]]] # used to avoid circular imports
    # makes me wanna KMSSSSSSSSS
    Pos = tuple[int, int] # [row][column]

    def __init__(self, pos: Pos, player: Player) -> None:
        super().__init__()
        self.pos: Piece.Pos = pos
        self.player: Player = player
        self.moved = False # enough pieces use this for me to not bother making different constructors

    def get_moves(self, board: t_board) -> list[Pos]:
        return []

class Pawn(Piece):
    def get_moves(self, board: Piece.t_board) -> list[Piece.Pos]:
        direction: int = -1 if self.player.name == "white" else 1
        row: int = self.pos[0] + direction
        moves: list[Piece.Pos] = []

        if row < 0 or row >= len(board):
            return moves

        # straight
        if board[row][self.pos[1]] is None:
            moves.append((row, self.pos[1]))

            if not self.moved and board[row + direction][self.pos[1]] is None:
                moves.append((row + direction, self.pos[1]))

        # diagonal
        for column in [i for i in [self.pos[1] - 1, self.pos[1] + 1] if i >= 0 and i < len(board)]:
            if board[row][column] is None:
                continue
            if board[row][column].player != self.player: # ignore error cuz already checked if None
                moves.append((row, column))

        # special thingy an pasant? TODO when I give more than half a ghasp of a fuck

        return moves

class Bishop(Piece):
    def get_moves(self, board: Piece.t_board) -> list[Piece.Pos]:
        moves: list[Piece.Pos] = []

        for dir in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            for pos in [(self.pos[0] + i * dir[0], self.pos[1] + i * dir[1]) for i in range(1, 8)]:
                if pos[0] < 0 or pos[0] >= len(board) or pos[1] < 0 or pos[1] >= len(board):
                    break
                if board[pos[0]][pos[1]] is None:
                    moves.append(pos)
                    continue
                if board[pos[0]][pos[1]].player != self.player:
                    moves.append(pos)
                break

        return moves

class Knight(Piece):
    def get_moves(self, board: Piece.t_board) -> list[Piece.Pos]:
        # why overcomplicate shidd?
        return [
            pos
            for pos in [
                ( self.pos[0] + 2, self.pos[1] + 1),
                (self.pos[0] + 2, self.pos[1] - 1),
                (self.pos[0] - 2, self.pos[1] + 1),
                (self.pos[0] - 2, self.pos[1] - 1),

                (self.pos[0] + 1, self.pos[1] + 2),
                (self.pos[0] + 1, self.pos[1] - 2),
                (self.pos[0] - 1, self.pos[1] + 2),
                (self.pos[0] - 1, self.pos[1] - 2),
            ]
            if (not(
                (pos[0] < 0 or pos[0] >= len(board)) or 
                (pos[1] < 0 or pos[1] >= len(board))
            ))
            and (
                board[pos[0]][pos[1]] is None
                or board[pos[0]][pos[1]].player != self.player
            )
        ]

class Rook(Piece):
    def get_moves(self, board: Piece.t_board) -> list[Piece.Pos]:
        moves: list[Piece.Pos] = []

        for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            for pos in [(self.pos[0] + i * dir[0], self.pos[1] + i * dir[1]) for i in range(1, 8)]:
                if pos[0] < 0 or pos[0] >= len(board) or pos[1] < 0 or pos[1] >= len(board):
                    break
                if board[pos[0]][pos[1]] is None:
                    moves.append(pos)
                    continue
                if board[pos[0]][pos[1]].player != self.player:
                    moves.append(pos)
                break

        return moves

class Queen(Piece):
    def get_moves(self, board: Piece.t_board) -> list[Piece.Pos]:
        return Bishop.get_moves(self, board) + Rook.get_moves(self, board)
        # my lsp sure doesn't like this however

class King(Piece):
    def __init__(self, pos: Piece.Pos, player: Player) -> None:
        super().__init__(pos, player)
        player.king = self

    def get_moves(self, board: Piece.t_board) -> list[Piece.Pos]:
        moves: list[Piece.Pos] = [
            pos
            for pos in [
                (self.pos[0] + 1, self.pos[1] + 1),
                (self.pos[0] + 1, self.pos[1] - 1),
                (self.pos[0] - 1, self.pos[1] + 1),
                (self.pos[0] - 1, self.pos[1] - 1),
            ]
            if (not(
                (pos[0] < 0 or pos[0] >= len(board)) or 
                (pos[1] < 0 or pos[1] >= len(board))
            ))
            and (
                board[pos[0]][pos[1]] is None
                or board[pos[0]][pos[1]].player != self.player
            )
        ]
        
        # TODO: add rokade

        return moves
