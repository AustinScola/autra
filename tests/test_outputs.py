"""Test the representation of player/agent outputs."""
from tetris.outputs import Outputs


def test_random() -> None:
    """Test generating random outputs."""
    random_outputs = Outputs.random()

    assert isinstance(random_outputs, Outputs)
