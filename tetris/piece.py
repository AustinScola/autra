"""A tetromino piece."""
from dataclasses import dataclass, replace
from typing import ClassVar, Dict

from tetris.orientation import Orientation
from tetris.rotation import Rotation


@dataclass(frozen=True)
class Piece:
    """A tetromino piece."""
    ROTATIONS: ClassVar[Dict[Orientation, Rotation]]
    orientation: Orientation

    @property
    def rotation(self) -> Rotation:
        """Return the current rotation of the piece based on the orientation."""
        return self.ROTATIONS[self.orientation]

    @property
    def rotated_clockwise(self) -> 'Piece':
        """Return the piece with an orientation that is rotated clockwise."""
        rotated_orientation = self.orientation.rotated_clockwise
        return replace(self, orientation=rotated_orientation)
