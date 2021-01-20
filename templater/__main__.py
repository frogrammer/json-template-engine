"""azkm CLI entry point."""

from templater.commands import *  # noqa
import firehelper

def main():
    """templater CLI.
    """

    start_cli()

def start_cli():
    firehelper.start_fire_cli('templater')

if __name__ == '__main__':
    main()
