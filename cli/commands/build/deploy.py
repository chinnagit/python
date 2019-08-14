
import click
import services
import collections
import functools


@click.group('deploy')
@click.pass_context
def deploy_group(ctx, **kwargs):
    """deploy docker-related tools."""
    projects = collections.OrderedDict()
    for p_cls in services.list_all():
        projects[p_cls.name] = functools.partial(p_cls.project_from_click_context, ctx, **kwargs)

    print 'projects ', projects
    ctx.obj['service_factories'] = projects
    pass


def make_deploy_command(project_cls):
    """
    :type project_cls: project.BaseProject
    :return:
    """
    @click.command(project_cls.name, help='deploy %s from ecommerce root' % project_cls.name)
    @click.pass_context
    def deploy_all_dev_backend(ctx):
        project = ctx.obj['service_factories'][project_cls.name]()
        # assert isinstance(project, services.BaseProject)

        project.deploy()

    return deploy_all_dev_backend


def define_deploy_commands():
    """ Generate stub commands for now to build all tools (as the build is the same).
        If we move e.g. r3 out of this cycle, we'll just extract r3 from here and implement differently.
    """
    for project_class in services.list_all():
        deploy_group.add_command(make_deploy_command(project_class))
    # deploy_group.add_command(aio.build)




define_deploy_commands()

if __name__ == '__main__':
    deploy_group()