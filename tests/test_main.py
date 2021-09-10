"""Test the main Tetris entry point."""
from typing import Any, List

import pytest

from tetris.main import main


# yapf: disable
@pytest.mark.parametrize('arguments', [
    ([]),
])
# yapf: enable
def test_main(arguments: List[Any]) -> None:
    """Test the main Tetris entry point."""
    main(arguments)
