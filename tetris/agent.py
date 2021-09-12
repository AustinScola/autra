"""A game playing agent."""
from typing import Any

from tetris.state import State


class Agent:
    """A game playing agent."""
    def start(self) -> None:
        """Start the agent."""

    def update(self, state: State) -> None:
        """Update the state that the agent is aware of."""

    @property
    def outputs(self) -> Any:
        """Return the outputs of the agent."""
        return None

    def end(self) -> None:
        """End the agent."""
