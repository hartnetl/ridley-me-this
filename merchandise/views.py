from django.shortcuts import render
from .models import Merch, Donate

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    merchandise = Merch.objects.all()
    donations = Donate.objects.all()
    
    context = {
        'merchandise': merchandise,
        'donations': donations,
    }

    return render(request, 'merchandise/merch.html', context)
