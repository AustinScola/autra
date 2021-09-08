"""Test the Tetris game state representation."""
from tetris.pieces import PIECES
from tetris.state import COLUMNS, HIDDEN_ROWS, ROWS, State


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

    assert len(state.playfield) == ROWS
    assert all(len(row) == COLUMNS for row in state.playfield)
