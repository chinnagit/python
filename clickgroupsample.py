import click


class AliasedGroup(click.Group):

    def get_command(self, ctx, cmd_name):
        rv = click.Group.get_command(self, ctx, cmd_name)
        if rv is not None:
            return rv
        matches = [x for x in self.list_commands(ctx)
                   if x.startswith(cmd_name)]
        if not matches:
            return None
        elif len(matches) == 1:
            return click.Group.get_command(self, ctx, matches[0])
        ctx.fail('Too many matches: %s' % ', '.join(sorted(matches)))

@click.command(cls=AliasedGroup)
def cli():
    pass

@cli.command()
def push():
    print 'called push'
    pass

@cli.command()
def pop():
    print 'called pop'
    pass

# @click.group()
# @click.option('--debug/--no-debug', default=False)
# def cli(debug):
#     print('Debug mode is %s' % ('on' if debug else 'off'))
#
#
# @cli.command()
# def sync():
#     print('Synching')
#     pass
#
# @cli.command()
# def build():
#     print('building')
#
# @cli.command()
# def docker():
#     print('create docker')


if __name__ == '__main__':
    cli()


