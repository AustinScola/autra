"""Test the tetromino piece representation."""
from typing import Any, Dict, List

import pytest

from tetris.orientation import Orientation, Up
from tetris.piece import Piece


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
