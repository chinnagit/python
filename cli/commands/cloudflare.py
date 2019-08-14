import click


@click.group()
def cloudflare():
    pass


@click.command()
def build():
    click.echo(' cloudflare1 This is mvn build command')
    pass


@click.command()
def docker():
    click.echo('cloudflare1 this is docker build command')