"""A tetromino piece."""
from typing import Dict

from tetris.orientation import Orientation
from tetris.rotation import Rotation


class Piece:  # pylint: disable=too-few-public-methods
    """A tetromino piece."""
    rotations = Dict[Orientation, Rotation]

    def __init__(self, orientation: Orientation) -> None:
        self.orientation = orientation

    @property
    def rotation(self) -> Rotation:
        """Return the current rotation of the piece based on the orientation."""
        return self.rotations[self.orientation]
