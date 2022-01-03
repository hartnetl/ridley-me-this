from django.shortcuts import render, reverse
from .models import Merch, Donate, Category


def all_merch(request):
    """ A view to show all products, including sorting and search queries """

    merchandise = Merch.objects.all()
    donations = Donate.objects.all()
    categories = None

    if request.GET:

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            merchandise = merchandise.filter(category__name__in=categories)
            donations = donations.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    context = {
        'merchandise': merchandise,
        'donations': donations,
        'current_categories': categories,
    }

    return render(request, 'merchandise/merchandise.html', context)
