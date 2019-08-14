import click
import build


class BuildEcommerce:
    ECOMMERCE_PATH = '/Users/bala_chinna/tutorials/ecommerce'
    ECOMMERCE_CART_PATH = '/Users/bala_chinna/tutorials/ecommerce/cart-service'
    ECOMMERCE_PRODUCT_PATH = '/Users/bala_chinna/tutorials/ecommerce/products-service'
    ECOMMERCE_GATEWAY_PATH = '/Users/bala_chinna/tutorials/ecommerce/gateway-oauth-resource'
    ECOMMERCE_PAYMENT_PATH = '/Users/bala_chinna/tutorials/ecommerce/payment-service'
    ECOMMERCE_SECURITY_PATH = '/Users/bala_chinna/tutorials/ecommerce/security-service'
    ECOMMERCE_EUREKA_PATH = '/Users/bala_chinna/tutorials/ecommerce/discovery-eureka-service'

    def __init__(self):
        print 'invoking build ecommerce'

    # @click.command()
    # @click.option('--module', default='all-in-one', help='Enter your module to build' )
    # @click.option('--module', prompt='Enter your module to build',
    #               help='Enter your module to build.')
    def buildmodule(ctx, module):
        print 'invoking build ecommerce main function for the module ', module, BuildEcommerce.ECOMMERCE_PATH
        if module == 'cart':
            print 'building cart'
            # return ctx
            build.build(BuildEcommerce.ECOMMERCE_CART_PATH)
        elif module == 'product':
            build.build(BuildEcommerce.ECOMMERCE_PRODUCT_PATH)
        elif module == 'payment':
            build.build(BuildEcommerce.ECOMMERCE_PAYMENT_PATH)
        elif module == 'security':
            build.build(BuildEcommerce.ECOMMERCE_SECURITY_PATH)
        elif module == 'gateway':
            build.build(BuildEcommerce.ECOMMERCE_GATEWAY_PATH)
        else:
            print 'building all in one'
            build.build(BuildEcommerce.ECOMMERCE_PATH)


if __name__ == '__main__':
    obj = BuildEcommerce()
    obj.buildmodule()



