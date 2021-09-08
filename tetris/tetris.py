"""The game of Tetris."""
from tetris.state import State


class Tetris:
    """The game of Tetris."""
    @staticmethod
    def play() -> None:
        """Play a game of tetris."""
        state: State = State()

        while True:
            state = Tetris.update(state)

    @staticmethod
    def update(state: State) -> State:
        """Update the state."""
        raise NotImplementedError
