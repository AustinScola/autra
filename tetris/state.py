"""The state of a Tetris game."""
from dataclasses import dataclass, replace
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

    def __getitem__(self, index: int) -> Tuple[bool, ...]:
        return self.grid[index]

    def lock_piece(self, piece: Piece, position: Position) -> 'Playfield':
        """Return the playfield with the given piece locked in the given position."""
        grid = self.grid

        for relative_block_position in piece.rotation:
            absolute_block_position = relative_block_position + position
            y, x = absolute_block_position.y, absolute_block_position.x  # pylint: disable=invalid-name
            grid = (*grid[:y], (*grid[y][:x], True, *grid[y][x + 1:]),
                    *grid[y + 1:])

        return Playfield(grid)


@dataclass(frozen=True)
class State:
    """The state of a Tetris game."""
    piece: Piece = random_piece()
    next_piece: Piece = random_piece()

    piece_position: Position = Position(5, 0)

    playfield: Playfield = Playfield()

    game_over: bool = False

    @property
    def can_drop_piece(self) -> bool:
        """Return if a piece can be dropped downwards in the playfield by one unit."""
        for block in self.piece.rotation:
            y = self.piece_position.y + block.y + 1  # pylint: disable=invalid-name
            x = self.piece_position.x + block.x  # pylint: disable=invalid-name

            if y >= 20 or self.playfield[y][x]:
                return False

        return True

    def lock_piece(self) -> 'State':
        """Return the state with the current piece locked at its position."""
        playfield = self.playfield.lock_piece(self.piece, self.piece_position)
        state = replace(self, playfield=playfield)
        return state

    def new_piece(self) -> 'State':
        """Return the state with next piece as the current piece and a new next piece."""
        state = replace(self,
                        piece=self.next_piece,
                        next_piece=random_piece(),
                        piece_position=Position(5, 0))
        return state

    def check_game_over(self) -> 'State':
        """Return the state which has been updated to reflect if the game is over."""
        # yapf: disable
        game_over: bool = any(
            self.playfield[block.y + self.piece_position.y][block.x + self.piece_position.x]
            for block in self.piece.rotation
        )
        # yapf: enable
        state = replace(self, game_over=game_over)
        return state
