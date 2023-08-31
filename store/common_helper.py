def cart_total_calculator(cart_items, shipping_charge):
    total = 0
    for item in cart_items:
        total += item.quantity*item.product.price
        
    return {
        'total': total+shipping_charge,
        'sub_total': total,
        'shipping_charge': shipping_charge
    }
