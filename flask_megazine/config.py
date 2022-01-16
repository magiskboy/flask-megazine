import os

class BaseConfiguration:
    DEBUG = False

    TESTING = False

    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")

    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SECRET_KEY = os.urandom(32)


class DevelopmentConfiguration(BaseConfiguration):
    DEBUG = True

    SECRET_KEY = 'secret key'


class TestConfiguration(BaseConfiguration):
    TESTING = True

    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class ProductionConfiguration(BaseConfiguration):
    ...


def get_config(config_name):
    if config_name == 'development':
        return DevelopmentConfiguration
    elif config_name == 'testing':
        return TestConfiguration
    else:
        return ProductionConfiguration
