"""Test the representation of a 2D integer position."""
import pytest

from tetris.position import Position


# yapf: disable
@pytest.mark.parametrize('position, other, expected_result', [
    (Position(0, 0), Position(0, 0), Position(0, 0)),
    (Position(1, 0), Position(0, 0), Position(1, 0)),
    (Position(1, 2), Position(3, 4), Position(4, 6)),
    (Position(1, 2), Position(-3, 4), Position(-2, 6)),
])
# yapf: enable
def test_add(position: Position, other: Position,
             expected_result: Position) -> None:
    """Test adding positions."""
    result: Position = position + other

    assert result == expected_result
