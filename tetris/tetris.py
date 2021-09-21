"""The game of Tetris."""
from dataclasses import replace
from time import sleep, time
from typing import Optional

from tetris.agent import Agent
from tetris.outputs import HorizontalOutput as HorizontalInput
from tetris.outputs import Outputs as Inputs
from tetris.position import Position
from tetris.renderer import Renderer
from tetris.state import State

FPS = 60.0988
FRAME_LENGTH = 1 / 60.0988


class Tetris:
    """The game of Tetris."""
    def __init__(self, renderer: Optional[Renderer] = None) -> None:
        self.renderer: Optional[Renderer] = renderer

    def play(self, agent: Agent) -> None:
        """Play a game of tetris."""
        if self.renderer is not None:  # pragma: no cover
            self.renderer.start()

        state: State = State()

        agent.start()
        agent.update(state)

        frame_start = time()
        while not state.game_over:
            inputs: Inputs = agent.outputs
            state = Tetris.update(state, inputs)

            if self.renderer is not None:  # pragma: no cover
                self.renderer.update(state)

            agent.update(state)

            sleep(FRAME_LENGTH - (time() - frame_start))
            frame_start = time()

        if self.renderer is not None:  # pragma: no cover
            self.renderer.end()

        agent.end()

    @staticmethod
    def update(state: State, inputs: Inputs) -> State:
        """Update the state."""
        if state.can_drop_piece:
            piece_position: Position = state.piece_position + Position(0, 1)
            state = replace(state, piece_position=piece_position)
        else:
            state = state.lock_piece()
            state = state.new_piece()
            state = state.check_game_over()

        if inputs.horizontal == HorizontalInput.LEFT:
            if state.can_shift_piece_left:
                state = state.shift_piece_left()
        elif inputs.horizontal == HorizontalInput.RIGHT:
            if state.can_shift_piece_right:
                state = state.shift_piece_right()

        if inputs.a and not inputs.b:
            if state.can_rotate_piece_clockwise:
                state = state.rotate_piece_clockwise()
        elif inputs.b and not inputs.a:
            if state.can_rotate_piece_counter_clockwise:
                state = state.rotate_piece_counter_clockwise()

        return state
