"""Test the tetris game."""
import pytest

from tetris.state import State
from tetris.tetris import Tetris


def test_play() -> None:
    """Test playing a game of Tetris."""
    tetris = Tetris()

    with pytest.raises(NotImplementedError):
        tetris.play()


def test_update() -> None:
    """Test updateing a game of Tetris."""
    state = State()

    with pytest.raises(NotImplementedError):
        Tetris.update(state)
