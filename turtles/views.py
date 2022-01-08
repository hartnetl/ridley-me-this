from django.shortcuts import render
from .models import Turtles

def turtles(request):
    """ A view to show turtle page with available and sponsored turtles """

    turtles = Turtles.objects.all()

    context = {
        'turtles': turtles,
    }

    return render(request, 'turtles/turtles.html', context)
