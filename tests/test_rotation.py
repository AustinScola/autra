"""Test the tetromino piece rotation representation."""
from typing import Set, Tuple

from tetris.rotation import Rotation


def test_rotation() -> None:
    """Test the tetromino piece rotation type alias."""
    assert Rotation == Set[Tuple[int, int]]
