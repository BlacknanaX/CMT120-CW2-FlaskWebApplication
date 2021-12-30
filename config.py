class Config:
    SECRET_KEY = 'Les Barbapapa'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


# class DevelopmentConfig(Config):
#     DEBUG = True
#     SQLALCHEMY_DATABASE_URI = 'mysql://c2050695:Blacknana985@csmysql.cs.cf.ac.uk:3306/c2050695_Blacknana'


# class TestingConfig(Config):
#     TESTING = True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://c2050695:Blacknana985@csmysql.cs.cf.ac.uk:3306/c2050695_Blacknana'


config = {
    # 'development': DevelopmentConfig,
    # 'test': TestingConfig,
    'production': ProductionConfig,

    'default': ProductionConfig

}
