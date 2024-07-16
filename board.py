from pieces import Piece, Pawn, Rook, Knight, Queen, King, Player, Bishop

from typing import Optional

# N for knight
STARTING_COMPOSITION: list[list[str]] = [
    ["BR", "BN", "BB", "BQ", "BK", "BB", "BN", "BR"],
    ["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP"],
    ["__", "__", "__", "__", "__", "__", "__", "__"],
    ["__", "__", "__", "__", "__", "__", "__", "__"],
    ["__", "__", "__", "__", "__", "__", "__", "__"],
    ["__", "__", "__", "__", "__", "__", "__", "__"],
    ["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP"],
    ["WR", "WN", "WB", "WQ", "WK", "WB", "WN", "WR"],
]

TESTING_COMPOSITION: list[list[str]] = [
    ["__", "__", "__", "__", "__", "__", "__", "__"],
    ["__", "__", "__", "__", "__", "__", "__", "__"],
    ["__", "__", "WP", "__", "__", "__", "BB", "__"],
    ["__", "__", "__", "__", "__", "__", "__", "__"],
    ["WN", "BR", "__", "__", "BQ", "__", "WR", "WN"],
    ["__", "__", "__", "__", "__", "WB", "__", "__"],
    ["__", "__", "__", "__", "__", "__", "__", "__"],
    ["__", "__", "__", "BK", "__", "__", "__", "__"],
]

class Board(list[list[Optional[Piece]]]):
    # board[rows(h -> a)][columns(1 -> 8)]
    def __init__(self, black: Player, white: Player) -> None:
        super().__init__([
            [
                Pawn((i, j), black if square[0] == "B" else white) if square[1] == "P" else # a bit too much repitition, but fugg it
                Rook((i, j), black if square[0] == "B" else white) if square[1] == "R" else
                Knight((i, j), black if square[0] == "B" else white) if square[1] == "N" else
                Bishop((i, j), black if square[0] == "B" else white) if square[1] == "B" else
                Queen((i, j), black if square[0] == "B" else white) if square[1] == "Q" else
                King((i, j), black if square[0] == "B" else white) if square[1] == "K" else
                None
                for j, square in enumerate(row)
            ] 
            for i, row in enumerate(TESTING_COMPOSITION)
        ])
