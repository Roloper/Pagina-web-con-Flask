class Config:
    SECRET_KEY = ''

class DevelopmentConfig():
    DEBUG = True

config ={
    'development' : DevelopmentConfig
}