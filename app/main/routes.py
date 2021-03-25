from app.main import bp
from flask import render_template, jsonify, current_app
from flask_login import login_required


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
        'publickey': current_app.config['STRIPE_PUBLISHABLE_KEY']
    }
    return jsonify(stripe_config)
