"""Test the agent which produces random outputs."""
from tetris.agent import Agent
from tetris.agents.random_outputs_agent import RandomOutputsAgent
from tetris.outputs import Outputs


def test_inheritance() -> None:
    """Test that the random outputs agent is an agent."""
    assert issubclass(RandomOutputsAgent, Agent)


def test_outputs() -> None:
    """Test the outputs of the random outputs agent."""
    random_outputs_agent = RandomOutputsAgent()

    outputs = random_outputs_agent.outputs

    assert isinstance(outputs, Outputs)
