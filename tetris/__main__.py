"""Package main."""
import sys

from tetris.main import main


def package_main() -> None:
    """Run with the system arguments."""
    if __name__ == '__main__':
        sys.exit(main(sys.argv[1:]))


package_main()
