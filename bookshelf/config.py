import os
class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqllite://'
    
class DevelopmentConfig(BaseConfig):
    DEUG = True
    TESTING = True
    ENV = "dev"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SECRET_KEY = "a9eec0e0-23b7-4788-9a92-318347b9a39f"
    
class StagingConfig(BaseConfig):
    DEUG = True
    TESTING = True
    ENV = "prod"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SECRET_KEY = "792842bc-c4df-4de1-9177-d5207bd9faa6"

    
class ProductionConfig(BaseConfig):
    DEUG = True
    TESTING = True
    ENV = "staging"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SECRET_KEY = "8c0caeb1-6bb2-4d2d-b057-596b2dcab18e"



    
class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqllte://'
    
config ={
    "dev": "bookhelf.config.DevelopmentConfig",
    "staging": "bookshelf.config.StagingConfig",
    "prod": "bookshelf.config.ProductionConfig",
    "default": "bookshelf.config.DevelopmentConfig"
}

def configure_app(app):
    config_name = os.getenv('FLASK_CONFIGURATION', 'default')
    app.config.from_object(config[config_name])
    app.config.from_pyfile('config.cfg', silent=True) 