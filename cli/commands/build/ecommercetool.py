import click
import collections
import functools
import services
import build
import docker
import deploy
import sys
import subprocess
import logging

logger = logging.getLogger('ecommercetool')


def make_click_group():
    # print 'invoking make_cli_group'

    @click.option('--debug/--no-debug', default=False, help='Set to increase verbosity', show_default=True)
    @click.pass_context
    def _cli(ctx, debug, **kwargs):
        projects = collections.OrderedDict()
        for p_cls in all_services:
            projects[p_cls.name] = functools.partial(p_cls.project_from_click_context, ctx, **kwargs)

        ctx.obj['service_factories'] = projects
        ctx.obj['debug'] = debug

    all_services = services.list_all()

    decorated_cli = _cli
    for p_cls in all_services:
        for option in p_cls.make_click_options():
            decorated_cli = option(decorated_cli)

    return click.group()(decorated_cli)


cli = make_click_group()


def main():
    # print 'invoking main'
    cols, _ = click.get_terminal_size()
    cli.add_command(build.build_group)
    cli.add_command(docker.docker_group)
    cli.add_command(deploy.deploy_group)
    # x = cli.__dict__
    # print 'cli options'
    # for y in x:
    #     print y
    try:
        cli(
            obj={},
            # auto_envvar_prefix='EPMPTOOL',
            max_content_width=cols
        )
    except (
            # exceptions.PrintableError,
            subprocess.CalledProcessError
    ) as e:
        print 'Error', e
        # logger.debug('Error:', exc_info=1)
        click.secho(str(e), fg='red', err=True, color='--color' in sys.argv or DEFAULT_USER_COLORS)
        sys.exit(1)
    except subprocess.CalledProcessError:
        print 'subprocess Error', subprocess.CalledProcessError
        sys.exit(1)
    except Exception as ex:
        print 'Unhandled exception, aborting program', ex

        # logger.exception('Unhandled exception, aborting program')
        sys.exit(1)


if __name__ == '__main__':
    main()
    # print cli
