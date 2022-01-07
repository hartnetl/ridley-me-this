from django.shortcuts import render


def turtles(request):
    """ A view to show turtle page with available and sponsored turtles """

    return render(request, 'turtles/turtles.html')
