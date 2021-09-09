"""Some playfields used in tests."""
from tetris.state import COLUMNS, ROWS, Playfield

FilledPlayfield = Playfield(tuple((True, ) * COLUMNS for _ in range(ROWS)))

# yapf: disable
PlayfieldWithJLockedAtSpawn = \
    Playfield(
        tuple((
            tuple(map(bool, (0, 0, 0, 0, 1, 1, 1, 0, 0, 0))),
            tuple(map(bool, (0, 0, 0, 0, 0, 0, 1, 0, 0, 0))),
            *((False, ) * COLUMNS for _ in range(ROWS - 2))
        ))
    )
# yapf: enable

# yapf: disable
PlayfieldWithTLockedAtMiddleBottom = \
    Playfield(
        tuple((
            *((False, ) * COLUMNS for _ in range(ROWS - 4)),
            tuple(map(bool, (0, 0, 0, 0, 1, 1, 1, 0, 0, 0))),
            tuple(map(bool, (0, 0, 0, 0, 0, 1, 0, 0, 0, 0))),
            *((False, ) * COLUMNS for _ in range(2))
        ))
    )
# yapf: enable
