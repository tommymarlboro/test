import os

from flask import Flask

def create_app(test_config=None):
    """ Создает и настраивает приложение"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev')



    if test_config is None:
        # загружает конфигурацию экземпляра, если она существует, когда не тестируется
        app.config.from_pyfile('config.py', silent=True)
    else:
        #загружает тестовую конфигурацию
        app.config.from_mapping(test_config)
        
    #проверка, существует ли папка
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import src
    app.register_blueprint(src.bp)

    return app
