import click
from commands import cloudflare


@click.group()
def cli():
    pass


cli.add_command(cloudflare.build)
cli.add_command(cloudflare.docker)

# cli = click.CommandCollection(sources=[cloudflare.build, cloudflare.docker])

if __name__ == '__main__':
    cli()