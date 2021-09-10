"""The game of Tetris."""
from dataclasses import replace
from typing import Optional

from tetris.position import Position
from tetris.renderer import Renderer
from tetris.state import State


class Tetris:
    """The game of Tetris."""
    def __init__(self, renderer: Optional[Renderer] = None) -> None:
        self.renderer: Optional[Renderer] = renderer

    def play(self) -> None:
        """Play a game of tetris."""
        if self.renderer is not None:  # pragma: no cover
            self.renderer.start()

        state: State = State()

        while not state.game_over:
            state = Tetris.update(state)

            if self.renderer is not None:  # pragma: no cover
                self.renderer.update(state)

        if self.renderer is not None:  # pragma: no cover
            self.renderer.end()

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
