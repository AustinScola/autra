"""Test the tetris game."""
from unittest.mock import Mock

import pytest

from test_data.playfields import PlayfieldWithTLockedAtMiddleBottom
from tetris.pieces import PIECES, J, T
from tetris.position import Position
from tetris.state import Playfield, State
from tetris.tetris import Tetris


def test_play() -> None:
    """Test playing a game of Tetris."""
    tetris = Tetris()

    tetris.play()


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('state, expected_new_state, expect_new_piece', [
    (State(T(), J(), Position(5, 0), Playfield()), State(T(), J(), Position(5, 1), Playfield()), False),
    (State(T(), J(), Position(5, 18), Playfield()), State(J(), Mock(), Position(5, 0), PlayfieldWithTLockedAtMiddleBottom), True),
])
# yapf: enable # pylint: enable=line-too-long
def test_update(state: State, expected_new_state: State,
                expect_new_piece: bool) -> None:
    """Test updating a game of Tetris."""
    new_state: State = Tetris.update(state)

    assert new_state.piece == expected_new_state.piece

    if expect_new_piece:
        assert type(state.next_piece) in PIECES
    else:
        assert new_state.next_piece == expected_new_state.next_piece

    assert new_state.piece_position == expected_new_state.piece_position
    assert new_state.playfield == expected_new_state.playfield
