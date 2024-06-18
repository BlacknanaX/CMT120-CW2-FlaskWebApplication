class Config:
    SECRET_KEY = 'Les Barbapapa'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_COMMENTS_PER_PAGE = 10

    @staticmethod
    def init_app(app):
        pass


# class DevelopmentConfig(Config):
#     DEBUG = True
#     SQLALCHEMY_DATABASE_URI = 'mysql://c2050695:Blacknana985@csmysql.cs.cf.ac.uk:3306/c2050695_Blacknana'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql://c2050695:Blacknana985@csmysql.cs.cf.ac.uk:3306/c2050695_Blacknana'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://c2050695:Blacknana985@csmysql.cs.cf.ac.uk:3306/c2050695_Blacknana'


config = {
    # 'development': DevelopmentConfig,
    'tests': TestingConfig,
    'production': ProductionConfig,

    'default': ProductionConfig

}
