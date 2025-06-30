from products.models.product import Product

def get_similar_products_based_on_history(user):
    from orders.models.order import OrderItem, Order
    purchased_product_ids = OrderItem.objects.filter(order__customer=user).values_list('product_id', flat=True)
    product_counter = {}
    for product_id in purchased_product_ids:
        product_counter[product_id] = product_counter.get(product_id, 0) + 1
    sorted_products = sorted(product_counter.items(), key=lambda x: x[1], reverse=True)
    top_product_ids = [prod_id for prod_id, _ in sorted_products[:3]]
    return Product.objects.filter(id__in=top_product_ids, is_active=True, stock__gt=0)

def is_product_in_stock(product_id):
    try:
        product = Product.objects.get(id=product_id)
        return product.stock > 0
    except Product.DoesNotExist:
        return False
