#! /usr/bin/env python3.6

"""
server.py
Stripe Sample.
Python 3.6 or newer required.
"""
import os
from flask import Flask, redirect, request

import stripe
# This is your test secret API key.
stripe.api_key = 'sk_test_51NtAH4AhTNodXMLTUprAYl9SP6l79qP7pt0mniY1PSwgBSHRhzdBbsuXMDqU3D3kTiKUbzVn9fA7alhMv4XwQ1zf002p36eBdK'

app = Flask(__name__,
            static_url_path='',
            static_folder='')

YOUR_DOMAIN = 'https://andrewgithb.github.io/shopping-demo/'

@app.route('/hoodie-buy', methods=['POST'])
#@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():

    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'price_1NtAOLAhTNodXMLT9JfmgVO1',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)

@app.route('/tee-buy', methods=['POST'])
#@app.route('/create-checkout-session', methods=['POST'])
def tee_checkout_session():

    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'price_1NtBYkAhTNodXMLTkGifzmWc',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)


@app.route('/short-buy', methods=['POST'])
#@app.route('/create-checkout-session', methods=['POST'])
def short_checkout_session():

    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'price_1NtC5cAhTNodXMLTTdonUZsC',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)

# @app.route('/create-checkout-session', methods=['POST'])
# def create_checkout_session():

#     try:
#         checkout_session = stripe.checkout.Session.create(
#             line_items=[
#                 {
#                     # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
#                     'price': 'price_1NtAOLAhTNodXMLT9JfmgVO1',
#                     'quantity': 1,
#                 },
#                 {
#                     'price': 'price_1NtBYkAhTNodXMLTkGifzmWc',
#                     'quantity': 1,
#                 },
#             ],
#             mode='payment',
#             success_url=YOUR_DOMAIN + '/success.html',
#             cancel_url=YOUR_DOMAIN + '/cancel.html',
#         )
#     except Exception as e:
#         return str(e)

#     return redirect(checkout_session.url, code=303)

if __name__ == '__main__':
    app.run(port=4242)