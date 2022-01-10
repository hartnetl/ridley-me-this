from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages
from turtles.models import Turtle
from .models import Merch, Donate, Category


def all_merch(request):
    """ A view to show all products, including sorting and search queries """

    merchandise = Merch.objects.all()
    donations = Donate.objects.all()
    turtles = Turtle.objects.all()

    categories = None
    query = None

    if request.GET:
        # search query
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('turtles'))

            merch_queries = Q(name__icontains=query) | Q(description__icontains=query)
            merchandise = merchandise.filter(merch_queries)
            donations = donations.filter(merch_queries)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            merchandise = merchandise.filter(category__name__in=categories)
            donations = donations.filter(category__name__in=categories)
            turtles = turtles.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    context = {
        'merchandise': merchandise,
        'donations': donations,
        'current_categories': categories,
        'search_term': query,
    }

    return render(request, 'merchandise/merchandise.html', context)


def merch_detail(request, merch_id):
    """ A view to show individual merchandise details """

    merch = get_object_or_404(Merch, pk=merch_id)

    context = {
        'merch': merch,
    }

    return render(request, 'merchandise/merch_detail.html', context)
