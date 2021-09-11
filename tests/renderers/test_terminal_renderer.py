"""Test the terminal renderer."""
from typing import Set
from unittest.mock import patch

import pytest
from _pytest.capture import CaptureFixture
from seligimus.standards.ansi.escape_codes.cursor import HIDE_CURSOR, SHOW_CURSOR
from seligimus.standards.ansi.escape_codes.screen import (DISABLE_ALTERNATIVE_SCREEN,
                                                          ENABLE_ALTERNATIVE_SCREEN)

from test_data.playfields import FilledPlayfield
from test_data.terminal_renderings import FILLED_PLAYFIELD_OUTPUT, JU_AT_2_3_PARTS
from tetris.orientation import Up
from tetris.piece import Piece
from tetris.pieces import J
from tetris.position import Position
from tetris.renderer import Renderer
from tetris.renderers.terminal_renderer import TerminalRenderer
from tetris.state import Playfield, State


def test_inheritance() -> None:
    """Test that the terminal renderer is a renderer."""
    assert issubclass(TerminalRenderer, Renderer)


def test_start(capsys: CaptureFixture) -> None:
    """Test that starting the terminal renderer enables an alternative screen."""
    terminal_renderer = TerminalRenderer()

    terminal_renderer.start()
    captured_output, _ = capsys.readouterr()

    assert list(captured_output) == list(HIDE_CURSOR +
                                         ENABLE_ALTERNATIVE_SCREEN)


# yapf: disable
@pytest.mark.parametrize('state', [
    (State(playfield=FilledPlayfield)),
])
# yapf: enable
def test_update(state: State) -> None:
    """Test rendering the state."""
    terminal_renderer = TerminalRenderer()

    # pylint: disable=line-too-long
    with patch('tetris.renderers.terminal_renderer.TerminalRenderer._draw_playfield') as draw_playfield_mock, \
        patch('tetris.renderers.terminal_renderer.TerminalRenderer._draw_piece') as draw_piece_mock:
        # pylint: enable=line-too-long

        terminal_renderer.update(state)

        draw_playfield_mock.assert_called_once()
        draw_piece_mock.assert_called_once()


# yapf: disable
@pytest.mark.parametrize('playfield, expected_output', [
    (FilledPlayfield, FILLED_PLAYFIELD_OUTPUT),
])
# yapf: enable
def test_draw_playfield(capsys: CaptureFixture, playfield: Playfield,
                        expected_output: str) -> None:
    """Test drawing the playfield."""
    TerminalRenderer._draw_playfield(playfield)  # pylint: disable=protected-access
    captured_output, _ = capsys.readouterr()

    assert list(captured_output) == list(expected_output)


# yapf: disable
@pytest.mark.parametrize('piece, position, expected_output', [
    (J(Up), Position(2, 3), JU_AT_2_3_PARTS)
])
# yapf: enable
def test_draw_piece(capsys: CaptureFixture, piece: Piece, position: Position,
                    expected_output: Set[str]) -> None:
    """Test drawing a piece at a position."""
    TerminalRenderer._draw_piece(piece, position)  # pylint: disable=protected-access
    captured_output, _ = capsys.readouterr()

    for part in expected_output:
        print(list(part), part in captured_output, list(captured_output))

    assert all(part in captured_output for part in expected_output)
    assert len(captured_output) == sum(len(value) for value in expected_output)


def test_end(capsys: CaptureFixture) -> None:
    """Test that ending the terminal renderer disables an alternative screen."""
    terminal_renderer = TerminalRenderer()

    terminal_renderer.end()
    captured_output, _ = capsys.readouterr()

    assert list(captured_output) == list(DISABLE_ALTERNATIVE_SCREEN +
                                         SHOW_CURSOR)
