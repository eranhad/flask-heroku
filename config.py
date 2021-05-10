import os

class Config:
    DEBUG = False
    DEVELOPMENT = False
    DB_PASS = os.getenv("DB_PASS", "this-is-the-default-value")

class ProductionConfig(Config):
    pass

class StagingConfig(Config):
    DEBUG = True

class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True