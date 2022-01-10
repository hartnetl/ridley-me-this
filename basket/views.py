from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from merchandise.models import Merch, Donate
from turtles.models import Turtle


def view_basket(request):
    """ A view that renders the shopping basket contents page """

    return render(request, 'basket/basket.html')


def add_merch_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping basket """

    merch = get_object_or_404(Merch, pk=item_id) 

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(request, f'Updated {merch.name} quantity to {basket[item_id]}')
    else:
        basket[item_id] = quantity
        messages.success(request, f'Added {merch.name} to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)
