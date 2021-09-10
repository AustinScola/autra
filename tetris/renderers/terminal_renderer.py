"""A renderer for the terminal."""
import sys

from seligimus.maths.integer_position_2d import IntegerPosition2D
from seligimus.standards.ansi.escape_codes.cursor import get_move_cursor
from seligimus.standards.ansi.escape_codes.screen import (DISABLE_ALTERNATIVE_SCREEN,
                                                          ENABLE_ALTERNATIVE_SCREEN)

from tetris.renderer import Renderer
from tetris.state import Playfield, State

BLOCK = '■ '
EMPTY = '  '


class TerminalRenderer(Renderer):
    """A renderer for the terminal."""
    def start(self) -> None:
        sys.stdout.write(ENABLE_ALTERNATIVE_SCREEN)
        sys.stdout.flush()

    def update(self, state: State) -> None:
        self._draw_playfield(state.playfield)

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

    def end(self) -> None:
        sys.stdout.write(DISABLE_ALTERNATIVE_SCREEN)
        sys.stdout.flush()
