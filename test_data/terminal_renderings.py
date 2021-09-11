"""Terminal rendering output test data."""
from tetris.renderers.terminal_renderer import BLOCK
from tetris.state import COLUMNS, ROWS

FILLED_PLAYFIELD_OUTPUT = \
    '\x1b[;H' + BLOCK * COLUMNS + \
    ''.join(f'\x1b[{row + 1};H' + BLOCK * COLUMNS for row in range(1, ROWS - 2))

JU_AT_2_3_PARTS = {
    '\x1b[3;3H' + BLOCK, '\x1b[4;3H' + BLOCK, '\x1b[4;5H' + BLOCK,
    '\x1b[4;7H' + BLOCK
}
