"""Test the tetromino piece representation."""
from typing import Any, Dict, List

import pytest

from tetris.orientation import Orientation, Up
from tetris.piece import Piece
from tetris.pieces import L
from tetris.rotation import Rotation


# yapf: disable
@pytest.mark.parametrize('arguments, keyword_arguments, expected_orientation', [
    ([Up], {}, Up),
])
# yapf: enable
def test_init(arguments: List[Any], keyword_arguments: Dict[str, Any],
              expected_orientation: Orientation) -> None:
    """Test initializing a piece."""
    piece = Piece(*arguments, **keyword_arguments)

    assert piece.orientation == expected_orientation


# yapf: disable
@pytest.mark.parametrize('piece, expected_rotation', [
    (L(Up), {(1, -1), (-1, 0), (0, 0), (1, 0)}),
])
# yapf: enable
def test_rotation(piece: Piece, expected_rotation: Rotation) -> None:
    """Test getting the current rotation of a piece."""
    rotation: Rotation = piece.rotation

    assert rotation == expected_rotation
