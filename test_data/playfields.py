"""Some playfields used in tests."""
from tetris.state import COLUMNS, ROWS, Playfield

FilledPlayfield = Playfield(tuple((False, ) * COLUMNS for _ in range(ROWS)))
