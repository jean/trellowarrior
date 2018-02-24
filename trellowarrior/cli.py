# -*- coding: utf-8 -*-

"""Console script for trellowarrior."""

import click
from trellowarrior import main as trellowarrior_main 
from trellowarrior import parse_config


@click.command()
def main(args=None):
    """Console script for trellowarrior."""
    # TODO: make conf file location configurable
    if parse_config('conf/trellowarrior.conf'):
        trellowarrior_main()


if __name__ == "__main__":
    main()
