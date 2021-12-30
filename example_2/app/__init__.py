from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from config import Config
import logging
from logging.handlers import RotatingFileHandler
import os

app = Flask(__name__)
app.config.from_object(Config)

bootstrap = Bootstrap(app)
moment = Moment(app)

products = {
        'book': {
            'name': 'The Rational Male',
            'price': 13900,
        },
        'support': {
            'name': 'Being Alpha',
            'price': 20000,
            'per': 'hour',
            'adjustable_quantity': {
                'enabled': True,
                'minimum': 1,
                'maximum': 4
            },
        },
    }

if not app.debug:
    if app.config['LOG_TO_STDOUT']:
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        app.logger.addHandler(stream_handler)
    else:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler(
            'logs/stripe_flask.log',
            maxBytes=10240,
            backupCount=10
            )
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
            ))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Stripe Flask Integration')

from app import routes
