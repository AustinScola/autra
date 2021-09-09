"""A tetromino piece."""
from dataclasses import dataclass
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
