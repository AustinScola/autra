"""Tetromino pieces."""
from random import choice

from tetris.piece import Piece

# yapf: disable
from tetris.orientation import (SingleOrientation, DualOrientation, QuadOrientation,  # isort:skip
                                Identity, Horizontal, Vertical, Up, Right, Down, Left)
# yapf: enable


class I(Piece):  # pylint: disable=invalid-name,too-few-public-methods
    """The I tetromino piece."""
    rotations = {
        Vertical: {(0, -2), (0, -1), (0, 0), (0, 1)},
        Horizontal: {(-2, 0), (-1, 0), (0, 0), (1, 0)}
    }

    def __init__(self, orientation: DualOrientation = Horizontal) -> None:
        super().__init__(orientation)


class J(Piece):  # pylint: disable=invalid-name,too-few-public-methods
    """The J tetromino piece."""
    rotations = {
        Up: {(-1, -1), (-1, 0), (0, 0), (1, 0)},
        Right: {(0, -1), (1, -1), (0, 0), (0, 1)},
        Down: {(-1, 0), (0, 0), (1, 0), (1, 1)},
        Left: {(0, -1), (0, 0), (-1, 1), (0, 1)}
    }

    def __init__(self, orientation: QuadOrientation = Down) -> None:
        super().__init__(orientation)


class L(Piece):  # pylint: disable=invalid-name,too-few-public-methods
    """The L tetromino piece."""
    rotations = {
        Up: {(1, -1), (-1, 0), (0, 0), (1, 0)},
        Right: {(0, -1), (0, 0), (0, 1), (1, 1)},
        Down: {(-1, 0), (0, 0), (1, 0), (-1, 1)},
        Left: {(-1, -1), (0, -1), (0, 0), (0, 1)}
    }

    def __init__(self, orientation: QuadOrientation = Down) -> None:
        super().__init__(orientation)


class O(Piece):  # pylint: disable=invalid-name,too-few-public-methods
    """The O tetromino piece."""
    rotations = {Identity: {(-1, 0), (0, 0), (-1, 1), (0, 1)}}

    def __init__(self, orientation: SingleOrientation = Identity) -> None:
        super().__init__(orientation)


class S(Piece):  # pylint: disable=invalid-name,too-few-public-methods
    """The S tetromino piece."""
    rotations = {
        Horizontal: {(0, 0), (1, 0), (-1, 1), (0, 1)},
        Vertical: {(0, -1), (0, 0), (1, 0), (1, 1)}
    }

    def __init__(self, orientation: DualOrientation = Horizontal) -> None:
        super().__init__(orientation)


class T(Piece):  # pylint: disable=invalid-name,too-few-public-methods
    """The T tetromino piece."""
    rotations = {
        Up: {(-1, 0), (0, 0), (1, 0), (0, -1)},
        Right: {(0, -1), (0, 0), (1, 0), (0, 1)},
        Down: {(-1, 0), (0, 0), (1, 0), (0, 1)},
        Left: {(0, -1), (-1, 0), (0, 0), (0, 1)}
    }

    def __init__(self, orientation: QuadOrientation = Down) -> None:
        super().__init__(orientation)


class Z(Piece):  # pylint: disable=invalid-name,too-few-public-methods
    """The Z tetromino piece."""
    rotations = {
        Vertical: {(-1, 0), (0, 0), (0, 1), (1, 1)},
        Horizontal: {(1, -1), (0, 0), (1, 0), (0, 1)}
    }

    def __init__(self, orientation: DualOrientation = Horizontal) -> None:
        super().__init__(orientation)


PIECES = {I, J, L, O, S, T, Z}
_PIECES_LIST = [I, J, L, O, S, T, Z]


def random_piece() -> Piece:
    """Return a random piece."""
    piece_type = choice(_PIECES_LIST)
    piece = piece_type()
    return piece
