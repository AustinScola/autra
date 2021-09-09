"""Tetromino pieces."""
from random import choice

from tetris.piece import Piece
from tetris.position import Position

# yapf: disable
from tetris.orientation import (SingleOrientation, DualOrientation, QuadOrientation,  # isort:skip
                                Identity, Horizontal, Vertical, Up, Right, Down, Left)
# yapf: enable


class I(Piece):  # pylint: disable=invalid-name,too-few-public-methods
    """The I tetromino piece."""
    # yapf: disable
    rotations = {
        Vertical: {Position(0, -2), Position(0, -1), Position(0, 0), Position(0, 1)},
        Horizontal: {Position(-2, 0), Position(-1, 0), Position(0, 0), Position(1, 0)}
    }
    # yapf: enable

    def __init__(self, orientation: DualOrientation = Horizontal) -> None:
        super().__init__(orientation)


class J(Piece):  # pylint: disable=invalid-name,too-few-public-methods
    """The J tetromino piece."""
    # yapf: disable
    rotations = {
        Up: {Position(-1, -1), Position(-1, 0), Position(0, 0), Position(1, 0)},
        Right: {Position(0, -1), Position(1, -1), Position(0, 0), Position(0, 1)},
        Down: {Position(-1, 0), Position(0, 0), Position(1, 0), Position(1, 1)},
        Left: {Position(0, -1), Position(0, 0), Position(-1, 1), Position(0, 1)}
    }
    # yapf: enable

    def __init__(self, orientation: QuadOrientation = Down) -> None:
        super().__init__(orientation)


class L(Piece):  # pylint: disable=invalid-name,too-few-public-methods
    """The L tetromino piece."""
    # yapf: disable
    rotations = {
        Up: {Position(1, -1), Position(-1, 0), Position(0, 0), Position(1, 0)},
        Right: {Position(0, -1), Position(0, 0), Position(0, 1), Position(1, 1)},
        Down: {Position(-1, 0), Position(0, 0), Position(1, 0), Position(-1, 1)},
        Left: {Position(-1, -1), Position(0, -1), Position(0, 0), Position(0, 1)}
    }
    # yapf: enable

    def __init__(self, orientation: QuadOrientation = Down) -> None:
        super().__init__(orientation)


class O(Piece):  # pylint: disable=invalid-name,too-few-public-methods
    """The O tetromino piece."""
    # yapf: disable
    rotations = {
        Identity: {Position(-1, 0), Position(0, 0), Position(-1, 1), Position(0, 1)}
    }
    # yapf: enable

    def __init__(self, orientation: SingleOrientation = Identity) -> None:
        super().__init__(orientation)


class S(Piece):  # pylint: disable=invalid-name,too-few-public-methods
    """The S tetromino piece."""
    # yapf: disable
    rotations = {
        Horizontal: {Position(0, 0), Position(1, 0), Position(-1, 1), Position(0, 1)},
        Vertical: {Position(0, -1), Position(0, 0), Position(1, 0), Position(1, 1)}
    }
    # yapf: enable

    def __init__(self, orientation: DualOrientation = Horizontal) -> None:
        super().__init__(orientation)


class T(Piece):  # pylint: disable=invalid-name,too-few-public-methods
    """The T tetromino piece."""
    # yapf: disable
    rotations = {
        Up: {Position(-1, 0), Position(0, 0), Position(1, 0), Position(0, -1)},
        Right: {Position(0, -1), Position(0, 0), Position(1, 0), Position(0, 1)},
        Down: {Position(-1, 0), Position(0, 0), Position(1, 0), Position(0, 1)},
        Left: {Position(0, -1), Position(-1, 0), Position(0, 0), Position(0, 1)}
    }
    # yapf: enable

    def __init__(self, orientation: QuadOrientation = Down) -> None:
        super().__init__(orientation)


class Z(Piece):  # pylint: disable=invalid-name,too-few-public-methods
    """The Z tetromino piece."""
    # yapf: disable
    rotations = {
        Vertical: {Position(-1, 0), Position(0, 0), Position(0, 1), Position(1, 1)},
        Horizontal: {Position(1, -1), Position(0, 0), Position(1, 0), Position(0, 1)}
    }
    # yapf: enable

    def __init__(self, orientation: DualOrientation = Horizontal) -> None:
        super().__init__(orientation)


PIECES = {I, J, L, O, S, T, Z}
_PIECES_LIST = [I, J, L, O, S, T, Z]


def random_piece() -> Piece:
    """Return a random piece."""
    piece_type = choice(_PIECES_LIST)
    piece = piece_type()
    return piece
