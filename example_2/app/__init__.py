from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from config import Config

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

from app import routes
