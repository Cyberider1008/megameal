import razorpay
from django.conf import settings

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

def create_razorpay_order(amount, currency='INR'):
    payment = client.order.create({
        'amount': int(amount * 100),
        'currency': currency,
        'payment_capture': '1'
    })
    return payment

def verify_signature(order_id, payment_id, signature):
    try:
        return client.utility.verify_payment_signature({
            'razorpay_order_id': order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
        })
    except razorpay.errors.SignatureVerificationError:
        return False
