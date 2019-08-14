
import click
import services
import opts
import collections
import functools


@click.group('build')
@click.pass_context
def build_group(ctx, **kwargs):
    """Build-related tools."""
    projects = collections.OrderedDict()
    for p_cls in services.list_all():
        projects[p_cls.name] = functools.partial(p_cls.project_from_click_context, ctx, **kwargs)

    print 'projects ', projects
    ctx.obj['service_factories'] = projects
    pass


def make_build_command(project_cls):
    """
    :type project_cls: project.BaseProject
    :return:
    """
    @click.command(project_cls.name, help='build %s from ecommerce root' % project_cls.name)
    @click.option(opts.BUILD_CLEAN, is_flag=True, default=True, **opts.BUILD_CLEAN_EXTRA)
    @click.option(opts.BUILD_THREADS_PER_CPU, type=int, **opts.BUILD_THREADS_PER_CPU_EXTRA)
    @click.pass_context
    def build_all_dev_backend(ctx, clean, threads_per_cpu):
        project = ctx.obj['service_factories'][project_cls.name]()
        # assert isinstance(project, services.BaseProject)

        project.build(clean, threads_per_cpu)

    return build_all_dev_backend


def define_build_commands():
    """ Generate stub commands for now to build all tools (as the build is the same).
        If we move e.g. r3 out of this cycle, we'll just extract r3 from here and implement differently.
    """
    for project_class in services.list_all():
        # print'srvice class', project_class
        build_group.add_command(make_build_command(project_class))
    # build_group.add_command(aio.build)
    # x = build_group.__dict__.get('commands')
    # for y in x:
    #     print y


define_build_commands()

if __name__ == '__main__':
    build_group()
