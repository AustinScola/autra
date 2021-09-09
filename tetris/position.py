"""A 2D integer position."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Position:
    """A 2D integer position."""
    x: int = 0  # pylint: disable=invalid-name
    y: int = 0  # pylint: disable=invalid-name

    def __add__(self, other: 'Position') -> 'Position':
        """Return the sum of the positions."""
        return Position(self.x + other.x, self.y + other.y)
