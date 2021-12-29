from django.shortcuts import render, reverse
from .models import Merch, Donate


def all_merch(request):
    """ A view to show all products, including sorting and search queries """

    merchandise = Merch.objects.all()
    donations = Donate.objects.all()

    context = {
        'merchandise': merchandise,
        'donations': donations,
    }

    return render(request, 'merchandise/merchandise.html', context)
