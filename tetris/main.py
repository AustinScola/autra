"""The main Tetris entry point."""
from typing import Any, List

from tetris.tetris import Tetris


def main(arguments: List[Any]) -> int:  # pylint: disable=unused-argument
    """Play a game of Tetris."""
    tetris = Tetris()

    tetris.play()

    return 0
