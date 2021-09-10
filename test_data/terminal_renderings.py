"""Terminal rendering output test data."""
from tetris.renderers.terminal_renderer import BLOCK
from tetris.state import COLUMNS, ROWS

FILLED_PLAYFIELD_OUTPUT = \
    '\x1b[;H' + BLOCK * COLUMNS + \
    ''.join(f'\x1b[{row + 1};H' + BLOCK * COLUMNS for row in range(1, ROWS - 2))
