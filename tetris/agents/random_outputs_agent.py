"""An agent which produces random outputs."""
from tetris.agent import Agent
from tetris.outputs import Outputs


class RandomOutputsAgent(Agent):
    """An agent which produces random outputs."""
    @property
    def outputs(self) -> Outputs:
        """Return random outputs."""
        return Outputs.random()
