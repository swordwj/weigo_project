import os
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig():  # 基本配置类
    AUTHOR = 'aolens'
    # SECRET_KEY = os.getenv('SECRET_KEY', 'DB_URI')


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    HOST = 'localhost'
    PORT = '5432'
    DATABASE = "weigodb"
    USER = "postgres"
    PASSWORD = "123456"
    # SQL_DATABASE_URI = 'postgresql://postgres:123456@localhost/weigo_testdb'


class TestingConfig(BaseConfig):
    TESTING = True
    HOST = 'localhost'
    PORT = '5432'
    DATABASE = "weigo_testdb"
    USER = "postgres"
    PASSWORD = "123456"
    # SQL_DATABASE_URI = 'postgresql://postgres:123456@localhost/weigo_testdb'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}