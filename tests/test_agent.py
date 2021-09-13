"""Test the representation of an agent."""
from unittest.mock import Mock

import pytest

from tetris.agent import Agent
from tetris.outputs import Outputs
from tetris.state import State


def test_start() -> None:
    """Test starting an agent."""
    mock_self = Mock()

    Agent.start(mock_self)


# yapf: disable
@pytest.mark.parametrize('state', [
    (State()),
])
# yapf: enable
def test_update(state: State) -> None:
    """Test providing an agent with a state update."""
    mock_self = Mock()

    Agent.update(mock_self, state)


def test_outputs() -> None:
    """Test getting outputs from an agent."""
    agent = Agent()

    outputs = agent.outputs

    assert isinstance(outputs, Outputs)


def test_end() -> None:
    """Test ending an agent."""
    mock_self = Mock()

    Agent.end(mock_self)
