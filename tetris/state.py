"""The state of a Tetris game."""
from dataclasses import dataclass

from seligimus.maths.integer_position_2d import IntegerPosition2D as Position

from tetris.piece import Piece
from tetris.pieces import random_piece

ROWS = 22
HIDDEN_ROWS = 2
COLUMNS = 10


@dataclass
class State:
    """The state of a Tetris game."""
    piece: Piece = random_piece()
    next_piece: Piece = random_piece()

    piece_position: Position = Position(5, 0)

    playfield = [[False] * COLUMNS for _ in range(ROWS)]
