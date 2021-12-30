# Integrate Stripe to Your Flask Application (with only Python; no Javascript)

![Stripe in Flask](example_2/app/static/images/stripe.gif)

## Features

* Stripe payment
* Localhost testing

## Tools Used

* Stripe API
* Flask framework
* Python for programming
* Flask bootstrap for styling and cross-browser compatibility
* Ngrok to test your locally running app on another device

## Installation

1. Clone this repo:

```python
$ git clone git@github.com:GitauHarrison/integrating-stripe-payment-in-flask.git
```

2. Change directory

```python
$ cd integrating-stripe-payment-in-flask/example_2
```

3. Create and activate a virtual environment

```python
$ mkvirtualenv stripe_env # I am using virtualenvwrapper
```

4. Install dependencies

```python
(stripe_env) $ pip3 install -r requirements.txt
```

5. Needed environment variables: 
   - Create a `.env` file in the root directory.

        ```python
        (stripe_env) $ touch .env
        ```
    - Add environment variables as seen in `.env.template`
        ```python
        STRIPE_SECRET_KEY=
        STRIPE_PUBLISHABLE_KEY=
        STRIPE_WEBHOOK_SECRET=
        SECRET_KEY=
        ```
        - If you are not aware of how to get these keys, consider going through [this simple guide](https://github.com/GitauHarrison/notes/blob/master/how_to_use_stripe_for_payment.md) (especially the section _Adding stripe_).
        - Best to create your `SECRET_KEY` value by running `python -c "import os; print(os.urandom(24))"` on your terminal. Copy the value and paste it into the `.env` file.
        <br>
5. Run the application

```python
(stripe_env) $ flask run
```

If you would like to test the example_2 application on another device other than your local machine, consider downloading `ngrok` as follows:

* On your terminal, run:

```python
(stripe_env) $ ngrok http 5000
```

You will see ngrok being downloaded, then you will have:

```python
ngrok by @inconshreveable                                                                (Ctrl+C to quit)
                                                                                                         
Session Status                online                                                                     
Account                       Gitau Harrison (Plan: Free)                                                
Version                       2.3.40                                                                     
Region                        United States (us)                                                         
Web Interface                 http://127.0.0.1:4040                                                      
Forwarding                    http://98f2-41-212-123-32.ngrok.io -> http://localhost:5000                
Forwarding                    https://98f2-41-212-123-32.ngrok.io -> http://localhost:5000               
                                                                                                         
Connections                   ttl     opn     rt1     rt5     p50     p90                                
                              0       0       0.00    0.00    0.00    0.00
```

Pay attention to the lines beginning with the word _Forwarding_. These are the lines that show the public URLs being mapped to your localhost. Paste, for example, `https://98f2-41-212-123-32.ngrok.io` into the browser of another device to test the application. You should be able to see the application running on your new device. Kindly note that if you have not [signed up for `ngrok`](https://dashboard.ngrok.com/signup), you will need to do so to use this feature.
<hr>
Cheers!