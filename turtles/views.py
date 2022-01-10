from django.shortcuts import render, get_object_or_404
from .models import Turtle


def turtles(request):
    """ A view to show turtle page with available and sponsored turtles """

    turtles = Turtle.objects.all()

    context = {
        'turtles': turtles,
    }

    return render(request, 'turtles/turtles.html', context)


def turtle_detail(request, turtle_id):
    """ A view to show each turtle in more detail """

    turtle = get_object_or_404(Turtle, pk=turtle_id)

    context = {
        'turtle': turtle,
    }

    return render(request, 'turtles/turtle_detail.html', context)