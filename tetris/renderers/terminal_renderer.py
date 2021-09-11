"""A renderer for the terminal."""
import sys

from seligimus.maths.integer_position_2d import IntegerPosition2D
from seligimus.standards.ansi.escape_codes.cursor import HIDE_CURSOR, SHOW_CURSOR, get_move_cursor
from seligimus.standards.ansi.escape_codes.screen import (DISABLE_ALTERNATIVE_SCREEN,
                                                          ENABLE_ALTERNATIVE_SCREEN)

from tetris.piece import Piece
from tetris.position import Position
from tetris.renderer import Renderer
from tetris.state import Playfield, State

BLOCK = '■ '
EMPTY = '  '
UNIT_SIZE = 2


class TerminalRenderer(Renderer):
    """A renderer for the terminal."""
    def start(self) -> None:
        sys.stdout.write(HIDE_CURSOR)
        sys.stdout.write(ENABLE_ALTERNATIVE_SCREEN)
        sys.stdout.flush()

    def update(self, state: State) -> None:
        self._draw_playfield(state.playfield)
        self._draw_piece(state.piece, state.piece_position)

    @staticmethod
    def _draw_playfield(playfield: Playfield) -> None:
        """Draw a playfield."""
        for row_number, row in enumerate(playfield.visible_rows):

            start_of_row_position = IntegerPosition2D(0, row_number)
            move_cursor: str = get_move_cursor(start_of_row_position)

            row_string = move_cursor + ''.join(BLOCK if filled else EMPTY
                                               for filled in row)
            sys.stdout.write(row_string)
        sys.stdout.flush()

    @staticmethod
    def _draw_piece(piece: Piece, position: Position) -> None:
        """Draw a piece at the given position."""
        rotation = piece.rotation
        for block_relative_position in rotation:
            block_absolute_position = position + block_relative_position
            x = UNIT_SIZE * block_absolute_position.x  # pylint: disable=invalid-name
            y = block_absolute_position.y  # pylint: disable=invalid-name
            move_cursor = get_move_cursor(IntegerPosition2D(x, y))
            sys.stdout.write(move_cursor + BLOCK)
        sys.stdout.flush()

    def end(self) -> None:
        sys.stdout.write(DISABLE_ALTERNATIVE_SCREEN)
        sys.stdout.write(SHOW_CURSOR)
        sys.stdout.flush()
