"""A renderer of state."""
from abc import ABC

from tetris.state import State


class Renderer(ABC):
    """A renderer of state."""
    def start(self) -> None:
        """Start the renderer."""

    def update(self, state: State) -> None:
        """Update the rendering based on the state."""

    def end(self) -> None:
        """End the renderer."""
