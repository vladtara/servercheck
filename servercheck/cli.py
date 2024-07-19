import click
import json
import sys


@click.command(no_args_is_help=True)
@click.option(
    "--filename", "-f", default=None, type=click.Path(), help="Json file to read"
)
@click.option(
    "--server", "-s", default=None, multiple=True, type=str, help="Server to check"
)
def cli(filename, server):
    data = set()
    if filename:
        try:
            with open(filename) as f:
                {data.add(i) for i in json.load(f)}
        except FileNotFoundError:
            click.echo(f"File {filename} not found")
            sys.exit(1)

    if server:
        {data.add(i) for i in server}

    click.echo(f"Data: {data}")


if __name__ == "__main__":
    cli()
