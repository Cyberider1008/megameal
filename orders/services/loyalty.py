from accounts.models.user import CustomUser

def award_loyalty_points(order):
    if order.payment_status == 'PAID' and not order.loyalty_points_awarded:
        points = int(order.total_price // 100)  # 1 point per ₹100
        user = order.customer
        user.loyalty_points += points
        user.save()
        order.loyalty_points_awarded = points
        order.save()
