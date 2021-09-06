"""Test the tetris game."""
import pytest

from tetris.tetris import Tetris


def test_play() -> None:
    """Test playing a game of Tetris."""
    tetris = Tetris()

    with pytest.raises(NotImplementedError):
        tetris.play()
