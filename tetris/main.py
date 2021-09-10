"""The main Tetris entry point."""
from typing import Any, List

from tetris.renderers.terminal_renderer import TerminalRenderer
from tetris.tetris import Tetris


def main(arguments: List[Any]) -> int:  # pylint: disable=unused-argument
    """Play a game of Tetris."""
    renderer = TerminalRenderer()
    tetris = Tetris(renderer)

    tetris.play()

    return 0
