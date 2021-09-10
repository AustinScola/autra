"""Test the abstract renderer."""
from unittest.mock import Mock

import pytest

from tetris.renderer import Renderer
from tetris.state import State


def test_start() -> None:
    """Test starting the abstract renderer."""
    mock_self = Mock(Renderer)
    Renderer.start(mock_self)


# yapf: disable
@pytest.mark.parametrize('state', [
    (State()),
])
# yapf: enable
def test_update(state: State) -> None:
    """Test updating the abstract renderer."""
    mock_self = Mock(Renderer)
    Renderer.update(mock_self, state)


def test_end() -> None:
    """Test end the abstract renderer."""
    mock_self = Mock(Renderer)
    Renderer.end(mock_self)
