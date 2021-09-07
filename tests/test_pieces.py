"""Test the tetromino pieces."""
from typing import Any, Dict, List

import pytest

from tetris.rotation import Rotation

# yapf: disable
from tetris.orientation import (SingleOrientation, DualOrientation, QuadOrientation,  # isort:skip
                                Identity, Horizontal, Vertical, Up, Right, Down, Left)
# yapf: enable

from tetris.pieces import I, J, L, O, S, T, Z  # isort:skip


# yapf: disable
@pytest.mark.parametrize('orientation, expected_rotation', [
    (Vertical, {(0, -2), (0, -1), (0, 0), (0, 1)}),
    (Horizontal, {(-2, 0), (-1, 0), (0, 0), (1, 0)}),
])
# yapf: enable
def test_i_rotations(orientation: DualOrientation,
                     expected_rotation: Rotation) -> None:
    """Test the I piece orientation to rotation mapping."""
    assert I.rotations[orientation] == expected_rotation


# yapf: disable
@pytest.mark.parametrize('arguments, keyword_arguments, expected_orientation', [
    ([Vertical], {}, Vertical),
    ([], {'orientation': Vertical}, Vertical),
    ([], {}, Horizontal),
])
# yapf: enable
def test_i_init(arguments: List[Any], keyword_arguments: Dict[str, Any],
                expected_orientation: DualOrientation) -> None:
    """Test initializing an I piece."""
    i = I(*arguments, **keyword_arguments)

    assert i.orientation == expected_orientation


# yapf: disable
@pytest.mark.parametrize('orientation, expected_rotation', [
    (Up, {(-1, -1), (-1, 0), (0, 0), (1, 0)}),
    (Right, {(0, -1), (1, -1), (0, 0), (0, 1)}),
    (Down, {(-1, 0), (0, 0), (1, 0), (1, 1)}),
    (Left, {(0, -1), (0, 0), (-1, 1), (0, 1)})
])
# yapf: enable
def test_j_rotations(orientation: QuadOrientation,
                     expected_rotation: Rotation) -> None:
    """Test the J piece orientation to rotation mapping."""
    assert J.rotations[orientation] == expected_rotation


# yapf: disable
@pytest.mark.parametrize('arguments, keyword_arguments, expected_orientation', [
    ([Up], {}, Up),
    ([], {'orientation': Up}, Up),
    ([], {}, Down),
])
# yapf: enable
def test_j_init(arguments: List[Any], keyword_arguments: Dict[str, Any],
                expected_orientation: QuadOrientation) -> None:
    """Test initializing a J piece."""
    j = J(*arguments, **keyword_arguments)

    assert j.orientation == expected_orientation


# yapf: disable
@pytest.mark.parametrize('orientation, expected_rotation', [
    (Up, {(1, -1), (-1, 0), (0, 0), (1, 0)}),
    (Right, {(0, -1), (0, 0), (0, 1), (1, 1)}),
    (Down, {(-1, 0), (0, 0), (1, 0), (-1, 1)}),
    (Left, {(-1, -1), (0, -1), (0, 0), (0, 1)})
])
# yapf: enable
def test_l_rotations(orientation: QuadOrientation,
                     expected_rotation: Rotation) -> None:
    """Test the L piece orientation to rotation mapping."""
    assert L.rotations[orientation] == expected_rotation


# yapf: disable
@pytest.mark.parametrize('arguments, keyword_arguments, expected_orientation', [
    ([Up], {}, Up),
    ([], {'orientation': Up}, Up),
    ([], {}, Down),
])
# yapf: enable
def test_l_init(arguments: List[Any], keyword_arguments: Dict[str, Any],
                expected_orientation: QuadOrientation) -> None:
    """Test initializing an L piece."""
    l = L(*arguments, **keyword_arguments)  # pylint: disable=invalid-name

    assert l.orientation == expected_orientation


# yapf: disable
@pytest.mark.parametrize('orientation, expected_rotation', [
    (Identity, {(-1, 0), (0, 0), (-1, 1), (0, 1)}),
])
# yapf: enable
def test_o_rotations(orientation: SingleOrientation,
                     expected_rotation: Rotation) -> None:
    """Test the O piece orientation to rotation mapping."""
    assert O.rotations[orientation] == expected_rotation


# yapf: disable
@pytest.mark.parametrize('arguments, keyword_arguments, expected_orientation', [
    ([Identity], {}, Identity),
    ([], {'orientation': Identity}, Identity),
    ([], {}, Identity),
])
# yapf: enable
def test_o_init(arguments: List[Any], keyword_arguments: Dict[str, Any],
                expected_orientation: QuadOrientation) -> None:
    """Test initializing an O piece."""
    o = O(*arguments, **keyword_arguments)  # pylint: disable=invalid-name

    assert o.orientation == expected_orientation


# yapf: disable
@pytest.mark.parametrize('orientation, expected_rotation', [
    (Horizontal, {(0, 0), (1, 0), (-1, 1), (0, 1)}),
    (Vertical, {(0, -1), (0, 0), (1, 0), (1, 1)})
])
# yapf: enable
def test_s_rotations(orientation: DualOrientation,
                     expected_rotation: Rotation) -> None:
    """Test the S piece orientation to rotation mapping."""
    assert S.rotations[orientation] == expected_rotation


# yapf: disable
@pytest.mark.parametrize('arguments, keyword_arguments, expected_orientation', [
    ([Vertical], {}, Vertical),
    ([], {'orientation': Vertical}, Vertical),
    ([], {}, Horizontal),
])
# yapf: enable
def test_s_init(arguments: List[Any], keyword_arguments: Dict[str, Any],
                expected_orientation: DualOrientation) -> None:
    """Test initializing an S piece."""
    s = S(*arguments, **keyword_arguments)  # pylint: disable=invalid-name

    assert s.orientation == expected_orientation


# yapf: disable
@pytest.mark.parametrize('orientation, expected_rotation', [
    (Up, {(-1, 0), (0, 0), (1, 0), (0, -1)}),
    (Right, {(0, -1), (0, 0), (1, 0), (0, 1)}),
    (Down, {(-1, 0), (0, 0), (1, 0), (0, 1)}),
    (Left, {(0, -1), (-1, 0), (0, 0), (0, 1)})
])
# yapf: enable
def test_t_rotations(orientation: DualOrientation,
                     expected_rotation: Rotation) -> None:
    """Test the T piece orientation to rotation mapping."""
    assert T.rotations[orientation] == expected_rotation


# yapf: disable
@pytest.mark.parametrize('arguments, keyword_arguments, expected_orientation', [
    ([Up], {}, Up),
    ([], {'orientation': Up}, Up),
    ([], {}, Down),
])
# yapf: enable
def test_t_init(arguments: List[Any], keyword_arguments: Dict[str, Any],
                expected_orientation: QuadOrientation) -> None:
    """Test initializing a T piece."""
    t = T(*arguments, **keyword_arguments)  # pylint: disable=invalid-name

    assert t.orientation == expected_orientation


# yapf: disable
@pytest.mark.parametrize('orientation, expected_rotation', [
    (Vertical, {(-1, 0), (0, 0), (0, 1), (1, 1)}),
    (Horizontal, {(1, -1), (0, 0), (1, 0), (0, 1)})
])
# yapf: enable
def test_z_rotations(orientation: DualOrientation,
                     expected_rotation: Rotation) -> None:
    """Test the Z piece orientation to rotation mapping."""
    assert Z.rotations[orientation] == expected_rotation


# yapf: disable
@pytest.mark.parametrize('arguments, keyword_arguments, expected_orientation', [
    ([Vertical], {}, Vertical),
    ([], {'orientation': Vertical}, Vertical),
    ([], {}, Horizontal),
])
# yapf: enable
def test_z_init(arguments: List[Any], keyword_arguments: Dict[str, Any],
                expected_orientation: DualOrientation) -> None:
    """Test initializing a Z piece."""
    z = Z(*arguments, **keyword_arguments)  # pylint: disable=invalid-name

    assert z.orientation == expected_orientation
