# config.py

class Config(object):
    """
    add config later

    """

class DevelopmentConfig(object):
    """
    add Dev config later

    """

    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(object):
    """
    add production config later

    """

    DEBUG = True

app_config = {
    'development' : DevelopmentConfig,
    'production' : ProductionConfig
}
