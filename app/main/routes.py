from app.main import bp
from flask import render_template, jsonify
from flask_login import login_required
from app import stripe_keys


@bp.route('/')
@bp.route('/home')
@login_required
def home():
    return render_template('home.html',
                           title='Home'
                           )


@bp.route('/config')
def get_publishable_key():
    stripe_config = {
        'publickey': stripe_keys['publishable_key']
    }
    return jsonify(stripe_config)
