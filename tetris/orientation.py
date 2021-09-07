"""Tetromino piece orientations."""
from typing import Type, Union


class _Orientation:  # pylint: disable=too-few-public-methods
    """A tetromino piece orientation."""
    rotated_clockwise: 'Orientation'
    rotated_counter_clockwise: 'Orientation'


Orientation = Type[_Orientation]


class Identity(_Orientation):  # pylint: disable=too-few-public-methods
    """The rotationally symmetrics orientation."""


Identity.rotated_clockwise = Identity
Identity.rotated_counter_clockwise = Identity

SingleOrientation = Union[Type[Identity]]


class Horizontal(_Orientation):  # pylint: disable=too-few-public-methods
    """The horizontal orientation."""


class Vertical(_Orientation):  # pylint: disable=too-few-public-methods
    """The vertical orientation."""


Vertical.rotated_clockwise = Horizontal
Vertical.rotated_counter_clockwise = Horizontal

Horizontal.rotated_clockwise = Vertical
Horizontal.rotated_counter_clockwise = Vertical

DualOrientation = Union[Type[Horizontal], Type[Vertical]]


class Up(_Orientation):  # pylint: disable=too-few-public-methods
    """The upwards orientation."""


class Right(_Orientation):  # pylint: disable=too-few-public-methods
    """The right orientation."""


class Left(_Orientation):  # pylint: disable=too-few-public-methods
    """The left orientation."""


class Down(_Orientation):  # pylint: disable=too-few-public-methods
    """The downwards orientation."""


Up.rotated_clockwise = Right
Up.rotated_counter_clockwise = Left

Right.rotated_clockwise = Down
Right.rotated_counter_clockwise = Up

Left.rotated_clockwise = Up
Left.rotated_counter_clockwise = Down

Down.rotated_clockwise = Left
Down.rotated_counter_clockwise = Right

QuadOrientation = Union[Type[Up], Type[Right], Type[Down], Type[Left]]
