"""Player or agent outputs."""
from dataclasses import dataclass
from enum import Enum, auto
from random import choice
from typing import Optional


class HorizontalOutput(Enum):
    """Horizonal direction pad output."""
    RIGHT = auto()
    LEFT = auto()


class VerticalOutput(Enum):
    """Vertical direction pad output."""
    UP = auto()
    DOWN = auto()


@dataclass(frozen=True)
class Outputs:
    """Player or agent outputs."""
    horizontal: Optional[HorizontalOutput] = None
    vertical: Optional[VerticalOutput] = None
    a: bool = False  # pylint: disable=invalid-name
    b: bool = False  # pylint: disable=invalid-name

    @staticmethod
    def random() -> 'Outputs':
        """Return random outputs."""
        horizontal = choice((None, *HorizontalOutput))
        vertical = choice((None, *VerticalOutput))
        a = choice((True, False))  # pylint: disable=invalid-name
        b = choice((True, False))  # pylint: disable=invalid-name

        return Outputs(horizontal, vertical, a, b)
