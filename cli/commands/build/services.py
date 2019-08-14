import subprocess

def list_all():
    """List all classes for microserves that this tool knows about."""
    return [
        Discovery,
        Products,
        Cart,
        Security,
        Zuul,
        Zipkin,
        Payment,
        Allinone
    ]


ECOMMERCE_PATH = '/Users/bala_chinna/tutorials/ecommerce'
ECOMMERCE_DISCOVERY_PATH = ECOMMERCE_PATH+'/discovery-eureka-service'
ECOMMERCE_ZUUL_PATH = ECOMMERCE_PATH+'/gateway-oauth-resource'
ECOMMERCE_ZIPKIN_PATH = ECOMMERCE_PATH+'/zipkin-service'
ECOMMERCE_SECURITY_PATH = ECOMMERCE_PATH+'/security-oauth-server'
ECOMMERCE_PRODUCTS_PATH = ECOMMERCE_PATH+'/products-service'
ECOMMERCE_UASER_PATH = ECOMMERCE_PATH+'/user-service'
ECOMMERCE_PAYMENT_PATH = ECOMMERCE_PATH+'/payment-service'
ECOMMERCE_CART_PATH = ECOMMERCE_PATH+'/cart-service'


class Discovery:
    name = 'discovery'
    imagename = 'ecommerce/' + name

    def __init__(self, xx):
        print 'discovery eureka service'

    def xx(self):
        print 'dummy discovery function'

    def build(self, ctx, debug, **cmd_kwargs):
        print 'build discovery eureka service'
        # build(ECOMMERCE_DISCOVERY_PATH)

    def builddocker(self):
        print 'building docker for discovery eureka service'
        createdockerimage(ECOMMERCE_DISCOVERY_PATH, Discovery.name+':1.0-SNAPSHOT')

    def deploy(self):
        print 'deploying ', Discovery.name

    @classmethod
    def project_from_click_context(cls, ctx, **cmd_kwargs):
        print '[Discovery] project_from_click_context'
        return cls('some value')

    @classmethod
    def make_click_options(cls):
        return []


class Zipkin:
    name = 'zipkin'
    imagename = 'ecommerce/' + name

    def __init__(self, xx):
        print 'Zipkin  service'

    def build(self, ctx, debug, **cmd_kwargs):
        print 'build Zipkin service'
        # build(ECOMMERCE_ZIPKIN_PATH)

    def builddocker(self):
        print 'building docker for Zipkin service'
        createdockerimage(ECOMMERCE_ZIPKIN_PATH, Zipkin.name+'service:1.0-SNAPSHOT')

    def deploy(self):
        print 'deploying ', Zipkin.name

    @classmethod
    def project_from_click_context(cls, ctx, **cmd_kwargs):
        print '[Zipkin] project_from_click_context'
        return cls('some value')

    @classmethod
    def make_click_options(cls):
        return []

class Zuul:
    name = 'apigateway'
    imagename = 'ecommerce/'+name

    def __init__(self, xx):
        print 'Zipkin  service'

    def build(self, ctx, debug, **cmd_kwargs):
        print 'build Zuul apigateway service'
        # build(ECOMMERCE_ZUUL_PATH)

    def builddocker(self):
        print 'building docker for Zuil apigateway service'
        createdockerimage(ECOMMERCE_ZUUL_PATH, Zuul.imagename+':1.0-SNAPSHOT')

    def deploy(self):
        print 'deploying ', Zuul.name

    @classmethod
    def project_from_click_context(cls, ctx, **cmd_kwargs):
        print '[Zuul] project_from_click_context'
        return cls('some value')

    @classmethod
    def make_click_options(cls):
        return []


class Security:
    name = 'security'
    imagename = 'securityoauthserver'

    def __init__(self, xx):
        print 'security  service'

    def build(self, ctx, debug, **cmd_kwargs):
        print 'build security service'
        # build(ECOMMERCE_SECURITY_PATH)

    def builddocker(self):
        print 'building docker for security oauth service'
        createdockerimage(ECOMMERCE_SECURITY_PATH, Security.imagename + ':1.0-SNAPSHOT')

    def deploy(self):
        print 'deploying ', Zuul.name

    @classmethod
    def project_from_click_context(cls, ctx, **cmd_kwargs):
        print '[Security] project_from_click_context'
        return cls('some value')

    @classmethod
    def make_click_options(cls):
        return []


class User:
    name = 'userservice'

    def __init__(self, xx):
        print 'user service'

    def build(self, ctx, debug, **cmd_kwargs):
        print 'build user service'
        # build(ECOMMERCE_UASER_PATH)

    def builddocker(self):
        print 'building docker for user service'
        createdockerimage(ECOMMERCE_UASER_PATH, User.name+':1.0-SNAPSHOT')

    def deploy(self):
        print 'deploying ', User.name

    @classmethod
    def project_from_click_context(cls, ctx, **cmd_kwargs):
        print '[cart] project_from_click_context'
        return cls('some value')

    @classmethod
    def make_click_options(cls):
        return []


class Cart:
    name = 'cartservice'
    imagename = 'ecommerce/' + name

    def __init__(self, xx):
        print 'cart service'

    def build(self, ctx, debug, **cmd_kwargs):
        print 'build cart service'
        # build(ECOMMERCE_CART_PATH)

    def builddocker(self):
        print 'building docker for cart service'
        createdockerimage(ECOMMERCE_CART_PATH, Cart.name+':1.0-SNAPSHOT')

    def deploy(self):
        print 'deploying ', Cart.name

    @classmethod
    def project_from_click_context(cls, ctx, **cmd_kwargs):
        print '[cart] project_from_click_context'
        return cls('some value')

    @classmethod
    def make_click_options(cls):
        return []


class Products:
    name = 'productsservice'

    def __init__(self, xx):
        print 'products service'

    def build(self, ctx, debug, **cmd_kwargs):
        print 'build products service'
        # build(ECOMMERCE_PRODUCTS_PATH)

    def builddocker(self):
        print 'building docker for products service'
        createdockerimage(ECOMMERCE_PRODUCTS_PATH, Products.name+':1.0-SNAPSHOT')

    def deploy(self):
        print 'deploying ', Products.name

    @classmethod
    def project_from_click_context(cls, ctx, **cmd_kwargs):
        print '[products] project_from_click_context'
        return cls('some value')

    @classmethod
    def make_click_options(cls):
        return []


class Payment:
    name = 'payment'

    def __init__(self, xx):
        print 'payment service'

    def build(self, ctx, debug, **cmd_kwargs):
        print 'build products service'
        # build(ECOMMERCE_PAYMENT_PATH)

    def builddocker(self):
        print 'building docker for payment service'
        createdockerimage(ECOMMERCE_PAYMENT_PATH, Payment.name+':1.0-SNAPSHOT')

    @classmethod
    def project_from_click_context(cls, ctx, **cmd_kwargs):
        print 'project_from_click_context'
        return cls('some value')

    @classmethod
    def make_click_options(cls):
        return []


class Allinone:
    name = 'allinone'

    def __init__(self, xx):
        print 'all in one service'

    def builddocker(self):
        print 'building docker for all in one service'
        for projclass in list_all():
            # print 'projclass.name', projclass.name
            if projclass.name == "allinone":
                continue
            else:
                yy = projclass(self)
                yy.builddocker()
        # createdockerimage(ECOMMERCE_PAYMENT_PATH, Payment.name+':1.0-SNAPSHOT')

    def deploy(self):
        print 'all in one deploy, uses docker-compose.yaml'
        deployall()

    def build(self, ctx, debug, **cmd_kwargs):
        print 'build all in one service'
        build(ECOMMERCE_PATH)
        Allinone.builddocker();
        # for projclass in list_all():
        #     # print 'projclass.name', projclass.name
        #     if projclass.name == "allinone":
        #         continue
        #     else:
        #         yy = projclass(self)
        #         yy.build(True, 2)

    @classmethod
    def project_from_click_context(cls, ctx, **cmd_kwargs):
        print '[Allinone] project_from_click_context'
        return cls('Allinone some value')

    @classmethod
    def make_click_options(cls):
        return []


def build(path):
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


def createdockerimage(path, imagename):
    dockercommand = 'docker build -t '+imagename+ ' '+path
    command = [dockercommand]
    # subprocess.check_call(command, shell=True)
    proc = subprocess.Popen(command,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            shell=True)
    out, err = proc.communicate()

    print("docker image command exit code: ", proc.returncode)
    print("docker command err: ", err)

    print("docker command stdout: ", out)


def deployall():
    # dockerdeploycommand = 'docker-compose -f '+ECOMMERCE_PATH+'/docker-compose-eureka-zipkin.yml up'
    dockerdeploycommand = 'docker-compose -f ' + ECOMMERCE_PATH + '/docker-compose-nomysql.yaml up'
    command = [dockerdeploycommand]
    print 'dockerdeploycommand: ', dockerdeploycommand
    # proc = subprocess.check_call(command, shell=True)
    proc = subprocess.Popen(command,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            shell=True)
    out, err = proc.communicate()

    print("docker compose command exit code: ", proc.returncode)
    print("docker compose command err: ", err)

    print("docker compose command stdout: ", out)