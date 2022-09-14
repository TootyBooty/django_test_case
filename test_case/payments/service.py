import stripe
from django.conf import settings
from django.urls import reverse

from .models import Item

stripe.api_key = settings.STRIPE_API_KEY


def create_checkout_session(path:str, item: Item):
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': settings.STRIPE_CURRENCY,
                    'product_data': {
                    'name': item.name,
                    },
                    'unit_amount': item.price.to_eng_string().replace('.', ''),
                },
                'quantity': 1,
                }],
            mode='payment',
            success_url = path + reverse('payments:success_payment'),
            cancel_url = path + reverse('payments:item_detail', args=[item.pk]),
        )
        return checkout_session
    except Exception as e:
        return str(e)














# def create_checkout_session(item_name:str, item_price:int):
#   session = stripe.checkout.Session.create(
#     line_items=[{
#       'price_data': {
#         'currency': settings.STRIPE_CURRENCY,
#         'product_data': {
#           'name': item_name,
#         },
#         'unit_amount': item_price,
#       },
#       'quantity': 1,
#     }],
#     mode='payment',
#     success_url='https://127.0.0.1:8000/success',
#     cancel_url='https://127.0.0.1:8000/cancel',
#   )