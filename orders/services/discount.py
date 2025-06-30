from django.utils import timezone

def apply_coupon(order, coupon):
    if not coupon.is_active or (coupon.expires_at and coupon.expires_at < timezone.now()):
        return 0.0
    if order.total_price < coupon.min_order_amount:
        return 0.0

    if coupon.discount_type == 'flat':
        return min(coupon.discount_value, order.total_price)
    elif coupon.discount_type == 'percent':
        return (coupon.discount_value / 100) * order.total_price
    return 0.0
