from django.shortcuts import render


def about_page(request):
    """ A view to show about info about the page and organisation """

    template = 'info/info.html'

    return render(request, template)

def learn_more(request):
    """ A view to show page where users can learn more about eco living, turtles etc """

    template = 'info/learn.html'

    return render(request, template)
