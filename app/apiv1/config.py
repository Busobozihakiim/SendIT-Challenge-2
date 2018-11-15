class BaseConfig:
    """Base app config"""
    DEBUG = False
    TESTING = False

class DevelopmentConfig(BaseConfig):
    """
    Development application configuration
    """
    DEBUG = True

class TestingConfig(BaseConfig):
    """
    Testing application configuration
    """
    DEBUG = False

class ProductionConfig(BaseConfig):
    """
    Production application configuration
    """
    DEBUG = False
    TESTING = False

configuration = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)