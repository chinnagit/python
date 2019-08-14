import click
from build_using_click import BuildEcommerce
import subprocess

# cli = click.Group()
#
# @cli.command()
# @click.option('--module', default='all-in-one', help='Enter your module to build' )
# def docker(module):
#     click.echo('docker moudle: %s' % module)
#
# @cli.command()
# @click.option('--module', default='all-in-one', help='Enter your module to build' )
# @click.pass_context
# def build(ctx, module):
#     print 'invoking build'
#     ctx.forward(docker)
#     # ctx.invoke(docker, module='product')


@click.group(invoke_without_command=True, chain=True)
@click.pass_context
def cli(ctx):
    sub = ctx.invoked_subcommand
    if ctx.invoked_subcommand is None:
        print('I was invoked without subcommand')
    elif sub == 'build':
        print('I am about to invoke %s' % ctx.invoked_subcommand)
    elif sub == 'docker':
        print 'invoking docker'


@cli.command()
@click.option('--module', default='all-in-one', help='Enter your module to build docker' )
# @click.pass_context
def docker(module):
    print('The docker subcommand for the module ', module)
    # ctx.forward(mvnbuild, module)
    # ctx.invoke(build(module))


@cli.command()
@click.option('--module', default='all-in-one', help='Enter your module to build' )
@click.pass_context
def build(ctx, module):
    print('The subcommand ', ' module: ', module)
    # obj = BuildEcommerce()
    # --module cart
    # ctx.forward(obj.buildmodule('cart'))
    # ctx.invoke(obj.buildmodule(module))
    # ctx.invoke(buildmodule(module))
    # ctx.forward(buildmodule, 'cart')
    # ctx.invoke(buildmodule())
    buildmodule(module)
    ctx.forward(docker, module)
    # pass




# def xx():
#     obj = BuildEcommerce()
#     obj.buildmodule()

# @cli.command()
# @click.option('--module', default='all-in-one', help='Enter your module to build' )
def buildmodule( module):
    print 'invoking build ecommerce main function for the module ', module, BuildEcommerce.ECOMMERCE_PATH
    if module == 'cart':
        print 'building cart'
        # return ctx
        mvnbuild(BuildEcommerce.ECOMMERCE_CART_PATH)
    elif module == 'product':
        mvnbuild(BuildEcommerce.ECOMMERCE_PRODUCT_PATH)
    elif module == 'payment':
        mvnbuild(BuildEcommerce.ECOMMERCE_PAYMENT_PATH)
    elif module == 'security':
        mvnbuild(BuildEcommerce.ECOMMERCE_SECURITY_PATH)
    elif module == 'gateway':
        mvnbuild(BuildEcommerce.ECOMMERCE_GATEWAY_PATH)
    else:
        print 'building all in one'
        mvnbuild(BuildEcommerce.ECOMMERCE_PATH)


def mvnbuild(path):
    mvncommand = 'mvn clean install -DskipTests -f '+path
    # command = ['mvn clean -f ~/work/epmp-user-directory/']
    command = [mvncommand]
    # subprocess.check_call(command, shell=True)
    proc = subprocess.Popen(command,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            shell=True)
    out, err = proc.communicate()

    print("exit code: ", proc.returncode)
    print("err: ", err)

    print("stdout: ", out)


if __name__ == '__main__':
    cli()
    # xx()