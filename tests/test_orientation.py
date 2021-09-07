"""Test the tetromino piece orientations."""
from typing import Type, Union

# yapf: disable
from tetris.orientation import (_Orientation, Orientation, SingleOrientation,  # isort:skip
                                DualOrientation,QuadOrientation, Identity, Horizontal, Vertical, Up,
                                Right, Down, Left)
# yapf: enable


def test_orientation() -> None:
    """Test the orientation type alias."""
    assert Orientation == Type[_Orientation]


def test_single_orientation() -> None:
    """Test the single orientation type alias."""
    assert SingleOrientation == Union[Type[Identity]]


def test_dual_orientation() -> None:
    """Test the dual orientation type alias."""
    assert DualOrientation == Union[Type[Horizontal], Type[Vertical]]


def test_quad_orientation() -> None:
    """Test the quad orientation type alias."""
    assert QuadOrientation == Union[Type[Up], Type[Right], Type[Down],
                                    Type[Left]]


def test_identity() -> None:
    """Test the identity orientation."""
    assert Identity.rotated_clockwise == Identity
    assert Identity.rotated_counter_clockwise == Identity


def test_horizontal() -> None:
    """Test the horizontal orientation."""
    assert Horizontal.rotated_clockwise == Vertical
    assert Horizontal.rotated_counter_clockwise == Vertical


def test_vertical() -> None:
    """Test the vertical orientation."""
    assert Vertical.rotated_clockwise == Horizontal
    assert Vertical.rotated_counter_clockwise == Horizontal


def test_up() -> None:
    """Test the upwards orientation."""
    assert Up.rotated_clockwise == Right
    assert Up.rotated_counter_clockwise == Left


def test_right() -> None:
    """Test the right orientation."""
    assert Right.rotated_clockwise == Down
    assert Right.rotated_counter_clockwise == Up


def test_down() -> None:
    """Test the downwards orientation."""
    assert Down.rotated_clockwise == Left
    assert Down.rotated_counter_clockwise == Right


def test_left() -> None:
    """Test the left orientation."""
    assert Left.rotated_clockwise == Up
    assert Left.rotated_counter_clockwise == Down
