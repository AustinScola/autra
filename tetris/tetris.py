"""The game of Tetris."""
from dataclasses import replace
from time import sleep, time
from typing import Optional

from tetris.position import Position
from tetris.renderer import Renderer
from tetris.state import State

FPS = 60.0988
FRAME_LENGTH = 1 / 60.0988


class Tetris:
    """The game of Tetris."""
    def __init__(self, renderer: Optional[Renderer] = None) -> None:
        self.renderer: Optional[Renderer] = renderer

    def play(self) -> None:
        """Play a game of tetris."""
        if self.renderer is not None:  # pragma: no cover
            self.renderer.start()

        state: State = State()

        frame_start = time()
        while not state.game_over:
            state = Tetris.update(state)

            if self.renderer is not None:  # pragma: no cover
                self.renderer.update(state)

            sleep(FRAME_LENGTH - (time() - frame_start))
            frame_start = time()

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
