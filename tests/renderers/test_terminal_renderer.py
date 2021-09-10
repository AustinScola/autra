"""Test the terminal renderer."""
import pytest
from _pytest.capture import CaptureFixture
from seligimus.standards.ansi.escape_codes.screen import (DISABLE_ALTERNATIVE_SCREEN,
                                                          ENABLE_ALTERNATIVE_SCREEN)

from test_data.playfields import FilledPlayfield
from test_data.terminal_renderings import FILLED_PLAYFIELD_OUTPUT
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

    assert list(captured_output) == list(ENABLE_ALTERNATIVE_SCREEN)


# yapf: disable
@pytest.mark.parametrize('state, expected_output', [
    (State(playfield=FilledPlayfield), FILLED_PLAYFIELD_OUTPUT),
])
# yapf: enable
def test_update(capsys: CaptureFixture, state: State,
                expected_output: str) -> None:
    """Test rendering the state."""
    terminal_renderer = TerminalRenderer()

    terminal_renderer.update(state)
    captured_output, _ = capsys.readouterr()

    assert list(captured_output) == list(expected_output)


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


def test_end(capsys: CaptureFixture) -> None:
    """Test that ending the terminal renderer disables an alternative screen."""
    terminal_renderer = TerminalRenderer()

    terminal_renderer.end()
    captured_output, _ = capsys.readouterr()

    assert list(captured_output) == list(DISABLE_ALTERNATIVE_SCREEN)
