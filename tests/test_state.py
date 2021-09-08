"""Test the Tetris game state representation."""
from seligimus.maths.integer_position_2d import IntegerPosition2D as Position

from tetris.pieces import PIECES
from tetris.state import COLUMNS, HIDDEN_ROWS, ROWS, Playfield, State


def test_rows() -> None:
    """Test the number of rows of the playfield."""
    assert ROWS == 22


def test_hidden_rows() -> None:
    """Test the number of hidden rows of the playfield."""
    assert HIDDEN_ROWS == 2


def test_columns() -> None:
    """Test the number of columns of the playfield."""
    assert COLUMNS == 10


def test_state_init() -> None:
    """Test initializing a Tetris game state."""
    state = State()

    assert type(state.piece) in PIECES
    assert type(state.next_piece) in PIECES

    assert state.piece_position == Position(5, 0)

    assert state.playfield == Playfield()


def test_playfield_init() -> None:
    """Test initializing a playfield."""
    playfield = Playfield()

    assert len(playfield) == ROWS
    assert all(len(row) == COLUMNS for row in playfield)


def test_playfield_len() -> None:
    """Test the length of a playfield."""
    playfield = Playfield()

    assert len(playfield) == ROWS
