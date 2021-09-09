"""Test the tetromino piece rotation representation."""
from typing import Set

from tetris.position import Position
from tetris.rotation import Rotation


def test_rotation() -> None:
    """Test the tetromino piece rotation type alias."""
    assert Rotation == Set[Position]
