from app.main import bp
from flask import render_template, jsonify, current_app, request
from flask_login import login_required
import stripe


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
        'publicKey': current_app.config['STRIPE_PUBLISHABLE_KEY']
    }
    return jsonify(stripe_config)


@bp.route('/create-checkout-session')
def create_checkout_session():
    domain_url = 'http://localhost:5000/'
    stripe.api_key = current_app.config['STRIPE_SECRET_KEY']
    try:
        checkout_session = stripe.checkout.Session.create(
            # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have
            # the session ID set as a query param
            # success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}'
            success_url=domain_url + 'success',
            cancel_url=domain_url + 'cancelled',
            payment_method_types=['card'],
            billing_address_collection='required',
            mode='payment',
            line_items=[
                {
                    'quantity': 1,
                    'price': 'price_1IYgbtFWpU2KHaPLODAVgoKU',
                }
            ]
        )
        return jsonify({'sessionId': checkout_session['id']})
    except Exception as e:
        return jsonify(error=str(e)), 403


@bp.route('/success')
def success():
    return render_template('success.html', title='Success')


@bp.route('/cancelled')
def cancel():
    return render_template('cancel.html', title='Cancel')


@bp.route("/webhook", methods=["POST"])
def stripe_webhook():
    payload = request.get_data(as_text=True)
    sig_header = request.headers.get("Stripe-Signature")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, current_app.config["STRIPE_ENDPOINT_SECRET"]
        )

    except ValueError as e:
        # Invalid payload
        return "Invalid payload", 400
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return "Invalid signature", 400

    # Handle the checkout.session.completed event
    if event["type"] == "checkout.session.completed":
        print("Payment was successful.")
        # TODO: you can run some custom code here

    return "Success", 200
