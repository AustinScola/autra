"""Tetromino pieces."""
from dataclasses import dataclass
from random import choice
from typing import ClassVar, Dict

from tetris.piece import Piece
from tetris.position import Position
from tetris.rotation import Rotation

# yapf: disable
from tetris.orientation import (Orientation, SingleOrientation, DualOrientation,  # isort:skip
                                QuadOrientation, Identity, Horizontal, Vertical, Up, Right, Down,
                                Left)
# yapf: enable


@dataclass(frozen=True)  # pylint: disable=invalid-name
class I(Piece):
    """The I tetromino piece."""
    # yapf: disable
    ROTATIONS: ClassVar[Dict[Orientation, Rotation]] = {
        Vertical: {Position(0, -2), Position(0, -1), Position(0, 0), Position(0, 1)},
        Horizontal: {Position(-2, 0), Position(-1, 0), Position(0, 0), Position(1, 0)}
    }
    # yapf: enable
    orientation: DualOrientation = Horizontal


@dataclass(frozen=True)  # pylint: disable=invalid-name
class J(Piece):
    """The J tetromino piece."""
    # yapf: disable
    ROTATIONS: ClassVar[Dict[Orientation, Rotation]] = {
        Up: {Position(-1, -1), Position(-1, 0), Position(0, 0), Position(1, 0)},
        Right: {Position(0, -1), Position(1, -1), Position(0, 0), Position(0, 1)},
        Down: {Position(-1, 0), Position(0, 0), Position(1, 0), Position(1, 1)},
        Left: {Position(0, -1), Position(0, 0), Position(-1, 1), Position(0, 1)}
    }
    # yapf: enable
    orientation: QuadOrientation = Down


@dataclass(frozen=True)  # pylint: disable=invalid-name
class L(Piece):
    """The L tetromino piece."""
    # yapf: disable
    ROTATIONS: ClassVar[Dict[Orientation, Rotation]] = {
        Up: {Position(1, -1), Position(-1, 0), Position(0, 0), Position(1, 0)},
        Right: {Position(0, -1), Position(0, 0), Position(0, 1), Position(1, 1)},
        Down: {Position(-1, 0), Position(0, 0), Position(1, 0), Position(-1, 1)},
        Left: {Position(-1, -1), Position(0, -1), Position(0, 0), Position(0, 1)}
    }
    # yapf: enable
    orientation: QuadOrientation = Down


@dataclass(frozen=True)  # pylint: disable=invalid-name
class O(Piece):
    """The O tetromino piece."""
    # yapf: disable
    ROTATIONS: ClassVar[Dict[Orientation, Rotation]] = {
        Identity: {Position(-1, 0), Position(0, 0), Position(-1, 1), Position(0, 1)}
    }
    # yapf: enable
    orientation: SingleOrientation = Identity


@dataclass(frozen=True)  # pylint: disable=invalid-name
class S(Piece):
    """The S tetromino piece."""
    # yapf: disable
    ROTATIONS: ClassVar[Dict[Orientation, Rotation]] = {
        Horizontal: {Position(0, 0), Position(1, 0), Position(-1, 1), Position(0, 1)},
        Vertical: {Position(0, -1), Position(0, 0), Position(1, 0), Position(1, 1)}
    }
    # yapf: enable
    orientation: DualOrientation = Horizontal


@dataclass(frozen=True)  # pylint: disable=invalid-name
class T(Piece):
    """The T tetromino piece."""
    # yapf: disable
    ROTATIONS: ClassVar[Dict[Orientation, Rotation]] = {
        Up: {Position(-1, 0), Position(0, 0), Position(1, 0), Position(0, -1)},
        Right: {Position(0, -1), Position(0, 0), Position(1, 0), Position(0, 1)},
        Down: {Position(-1, 0), Position(0, 0), Position(1, 0), Position(0, 1)},
        Left: {Position(0, -1), Position(-1, 0), Position(0, 0), Position(0, 1)}
    }
    # yapf: enable
    orientation: QuadOrientation = Down


@dataclass(frozen=True)  # pylint: disable=invalid-name
class Z(Piece):
    """The Z tetromino piece."""
    # yapf: disable
    ROTATIONS: ClassVar[Dict[Orientation, Rotation]] = {
        Vertical: {Position(-1, 0), Position(0, 0), Position(0, 1), Position(1, 1)},
        Horizontal: {Position(1, -1), Position(0, 0), Position(1, 0), Position(0, 1)}
    }
    # yapf: enable
    orientation: DualOrientation = Horizontal


PIECES = {I, J, L, O, S, T, Z}
_PIECES_LIST = [I, J, L, O, S, T, Z]


def random_piece() -> Piece:
    """Return a random piece."""
    piece_type = choice(_PIECES_LIST)
    piece = piece_type()
    return piece
