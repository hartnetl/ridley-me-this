from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from merchandise.models import Merch, Donate
from turtles.models import Turtle


def basket_contents(request):
    """
    This is a context processor.
    It is used to make this dictionary available to all templates across the
    entire application
    """
    basket_items = []
    total = 0
    item_count = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        merch = get_object_or_404(Merch, pk=item_id)
        donations = get_object_or_404(Donate, pk=item_id)
        # turtle = get_object_or_404(Turtle, pk=item_id)
        total += quantity * merch.price
        item_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'donations': donations,
            # 'turtle': turtle,
            'merch': merch
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'basket_items': basket_items,
        'total': total,
        'item_count': item_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
