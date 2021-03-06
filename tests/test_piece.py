"""Test the tetromino piece representation."""
from typing import Any, Dict, List

import pytest

from tetris.orientation import Left, Orientation, Right, Up
from tetris.piece import Piece
from tetris.pieces import L
from tetris.position import Position
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
    (L(Up), {Position(1, -1), Position(-1, 0), Position(0, 0), Position(1, 0)}),
])
# yapf: enable
def test_rotation(piece: Piece, expected_rotation: Rotation) -> None:
    """Test getting the current rotation of a piece."""
    rotation: Rotation = piece.rotation

    assert rotation == expected_rotation


# yapf: disable
@pytest.mark.parametrize('piece, expected_rotated_piece', [
    (L(Up), L(Right)),
])
# yapf: enable
def test_rotated_clockwise(piece: Piece,
                           expected_rotated_piece: Piece) -> None:
    """Test rotating a piece clockwise."""
    rotated_piece: Piece = piece.rotated_clockwise

    assert rotated_piece == expected_rotated_piece


# yapf: disable
@pytest.mark.parametrize('piece, expected_rotated_piece', [
    (L(Up), L(Left)),
])
# yapf: enable
def test_rotated_counter_clockwise(piece: Piece,
                                   expected_rotated_piece: Piece) -> None:
    """Test rotating a piece counter clockwise."""
    rotated_piece: Piece = piece.rotated_counter_clockwise

    assert rotated_piece == expected_rotated_piece
