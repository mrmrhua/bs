class Config:
        SECRET_KEY='you guess'

        SQLALCHEMY_COMMIT_ON_TEARDOWN = True

        @staticmethod
        def init_app(app):
            pass

        #配置不同环境
class DevelopmentConfig(Config):
    DEBUG = True
    sqluser = 'Coder'
    sqlpw = '123456'
    sqlhost = 'localhost'
    sqldb = 'bs'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + sqluser + ":" + \
                              sqlpw + "@" + sqlhost + "/" + sqldb

class TestingConfig(Config):
    pass

class ProductionConfig(Config):
    pass

config = {
    'development' : DevelopmentConfig,
    'testing' : TestingConfig,
    'production' : ProductionConfig,

    'default' : DevelopmentConfig
}