
import click
import services
import collections
import functools


@click.group('docker')
@click.pass_context
def docker_group(ctx, **kwargs):
    """docker-related tools."""
    projects = collections.OrderedDict()
    for p_cls in services.list_all():
        projects[p_cls.name] = functools.partial(p_cls.project_from_click_context, ctx, **kwargs)

    print 'projects ', projects
    ctx.obj['service_factories'] = projects
    pass


def make_docker_command(project_cls):
    """
    :type project_cls: project.BaseProject
    :return:
    """
    @click.command(project_cls.name, help='docker %s from ecommerce root' % project_cls.name)
    @click.pass_context
    def docker_all_dev_backend(ctx):
        project = ctx.obj['service_factories'][project_cls.name]()
        # assert isinstance(project, services.BaseProject)

        project.builddocker()

    return docker_all_dev_backend


def define_docker_commands():
    """ Generate stub commands for now to build all tools (as the build is the same).
        If we move e.g. r3 out of this cycle, we'll just extract r3 from here and implement differently.
    """
    for project_class in services.list_all():
        docker_group.add_command(make_docker_command(project_class))
    # docker_group.add_command(aio.build)




define_docker_commands()

if __name__ == '__main__':
    docker_group()