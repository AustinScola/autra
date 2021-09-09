"""The state of a Tetris game."""
from dataclasses import dataclass
from typing import Iterator, Tuple

from tetris.piece import Piece
from tetris.pieces import random_piece
from tetris.position import Position

ROWS = 22
HIDDEN_ROWS = 2
COLUMNS = 10


@dataclass(frozen=True)
class Playfield:
    """The playfield of a game of Tetris."""
    grid: Tuple[Tuple[bool, ...], ...] = tuple(
        (False, ) * COLUMNS for _ in range(ROWS))

    def __len__(self) -> int:
        """Return the number of rows."""
        return len(self.grid)

    def __iter__(self) -> Iterator[Tuple[bool, ...]]:
        return iter(self.grid)


@dataclass(frozen=True)
class State:
    """The state of a Tetris game."""
    piece: Piece = random_piece()
    next_piece: Piece = random_piece()

    piece_position: Position = Position(5, 0)

    playfield: Playfield = Playfield()
