"""The game of Tetris."""
from dataclasses import replace

from tetris.position import Position
from tetris.state import State


class Tetris:
    """The game of Tetris."""
    @staticmethod
    def play() -> None:
        """Play a game of tetris."""
        state: State = State()

        while not state.game_over:
            state = Tetris.update(state)

    @staticmethod
    def update(state: State) -> State:
        """Update the state."""
        if state.can_drop_piece:
            piece_position: Position = state.piece_position + Position(0, 1)
            state = replace(state, piece_position=piece_position)
        else:
            state = state.lock_piece()
            state = state.new_piece()
            state = state.check_game_over()

        return state
