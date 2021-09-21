"""Test the Tetris game state representation."""
from typing import Tuple

import pytest

from test_data.playfields import FilledPlayfield, PlayfieldWithJLockedAtSpawn
from tetris.orientation import Horizontal, Vertical
from tetris.piece import Piece
from tetris.pieces import PIECES, I, J, L, Z
from tetris.position import Position
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


# yapf: disable
@pytest.mark.parametrize('playfield, expected_visible_rows', [
    (FilledPlayfield, tuple((True, ) * COLUMNS for _ in range(ROWS - HIDDEN_ROWS))),
])
# yapf: enable
def test_playfield_visible_rows(
        playfield: Playfield, expected_visible_rows: Tuple[Tuple[bool, ...],
                                                           ...]) -> None:
    """Test the visible rows of a playfield."""
    visible_rows: Tuple[Tuple[bool, ...], ...] = playfield.visible_rows

    assert visible_rows == expected_visible_rows


def test_playfield_len() -> None:
    """Test the length of a playfield."""
    playfield = Playfield()

    assert len(playfield) == ROWS


# yapf: disable
@pytest.mark.parametrize('playfield, index, expected_row', [
    (Playfield(), 0, (False, ) * COLUMNS),
])
# yapf: enable
def test_playfield_get_item(playfield: Playfield, index: int,
                            expected_row: Tuple[bool, ...]) -> None:
    """Test accessing a row of the playfield."""
    row: Tuple[bool, ...] = playfield[index]

    assert row == expected_row


# yapf: disable
@pytest.mark.parametrize('playfield, piece, position, expected_playfield_after', [
    (Playfield(), J(), Position(5, 0), PlayfieldWithJLockedAtSpawn),
])
# yapf: enable
def test_playfield_lock_piece(playfield: Playfield, piece: Piece,
                              position: Position,
                              expected_playfield_after: Playfield) -> None:
    """Test locking a piece in the playfield."""
    playfield_after = playfield.lock_piece(piece, position)

    assert playfield_after == expected_playfield_after


# yapf: disable
@pytest.mark.parametrize('state, expected_value', [
    (State(), True),
    (State(playfield=FilledPlayfield), False),
    (State(piece=Z(), piece_position=Position(5, 18)), False),
])
# yapf: enable
def test_state_can_drop_piece(state: State, expected_value: bool) -> None:
    """Test the predicate which determines if the current piece can be dropped."""
    value: bool = state.can_drop_piece

    assert value == expected_value


# yapf: disable
@pytest.mark.parametrize('state, expected_value', [
    (State(), True),
    (State(L(), piece_position=Position(1, 0)), False),
])
# yapf: enable
def test_can_shift_piece_left(state: State, expected_value: bool) -> None:
    """Test the predicate which determines if the current piece can be shifted to the left."""
    value: bool = state.can_shift_piece_left

    assert value == expected_value


# yapf: disable
@pytest.mark.parametrize('state, expected_value', [
    (State(), True),
    (State(L(), piece_position=Position(8, 0)), False),
])
# yapf: enable
def test_can_shift_piece_right(state: State, expected_value: bool) -> None:
    """Test the predicate which determines if the current piece can be shifted to the right."""
    value: bool = state.can_shift_piece_right

    assert value == expected_value


# yapf: disable
@pytest.mark.parametrize('state, expected_value', [
    (State(), True),
    (State(playfield=FilledPlayfield), False),
    (State(I(Vertical), piece_position=Position(9, 0)), False),
])
# yapf: enable
def test_can_rotate_piece_counter_clockwise(state: State,
                                            expected_value: bool) -> None:
    """Test the predicate which determines if the current piece can be rotated counter clockwise."""
    value: bool = state.can_rotate_piece_counter_clockwise

    assert value == expected_value


# yapf: disable
@pytest.mark.parametrize('state, expected_value', [
    (State(), True),
    (State(playfield=FilledPlayfield), False),
    (State(I(Vertical), piece_position=Position(0, 0)), False),
])
# yapf: enable
def test_can_rotate_piece_clockwise(state: State,
                                    expected_value: bool) -> None:
    """Test the predicate which determines if the current piece can be rotated clockwise."""
    value: bool = state.can_rotate_piece_clockwise

    assert value == expected_value


# yapf: disable
@pytest.mark.parametrize('state, expected_state_after', [
    (State(I(), J()), State(I(), J(), Position(4, 0))),
])
# yapf: enable
def test_shift_piece_left(state: State, expected_state_after: State) -> None:
    """Test shifting the current piece to the left."""
    state_after = state.shift_piece_left()

    assert state_after == expected_state_after


# yapf: disable
@pytest.mark.parametrize('state, expected_state_after', [
    (State(I(), J()), State(I(), J(), Position(6, 0))),
])
# yapf: enable
def test_shift_piece_right(state: State, expected_state_after: State) -> None:
    """Test shifting the current piece to the right."""
    state_after = state.shift_piece_right()

    assert state_after == expected_state_after


# yapf: disable
@pytest.mark.parametrize('state, expected_state_after', [
    (State(I(Vertical), J()), State(I(Horizontal), J())),
])
# yapf: enable
def test_rotate_piece_clockwise(state: State,
                                expected_state_after: State) -> None:
    """Test rotating the current piece clockwise."""
    state_after = state.rotate_piece_clockwise()

    assert state_after == expected_state_after


# yapf: disable
@pytest.mark.parametrize('state, expected_state_after', [
    (State(I(Vertical), J()), State(I(Horizontal), J())),
])
# yapf: enable
def test_rotate_piece_counter_clockwise(state: State,
                                        expected_state_after: State) -> None:
    """Test rotating the current piece counter clockwise."""
    state_after = state.rotate_piece_counter_clockwise()

    assert state_after == expected_state_after


# yapf: disable
@pytest.mark.parametrize('state, expected_state_after', [
    (State(piece=J()), State(piece=J(), playfield=PlayfieldWithJLockedAtSpawn)),
])
# yapf: enable
def test_state_lock_piece(state: State, expected_state_after: State) -> None:
    """Test locking the piece of the state."""
    state_after = state.lock_piece()

    assert state_after == expected_state_after


# yapf: disable
@pytest.mark.parametrize('state', [
    (State(piece_position=Position(4, 10))),
])
# yapf: enable
def test_state_new_piece(state: State) -> None:
    """Test getting a new piece for the state."""
    new_state = state.new_piece()

    assert new_state.piece == state.next_piece
    assert new_state.piece_position == Position(5, 0)
    assert new_state.next_piece is not state.next_piece


# yapf: disable
@pytest.mark.parametrize('state, expected_new_state', [
    (State(playfield=FilledPlayfield), State(playfield=FilledPlayfield, game_over=True))
])
# yapf: enable
def test_state_check_game_over(state: State,
                               expected_new_state: State) -> None:
    """Test checking if the game is over based on the state."""
    new_state = state.check_game_over()

    assert new_state == expected_new_state
