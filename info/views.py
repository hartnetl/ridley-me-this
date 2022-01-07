from django.shortcuts import render


def about_page(request):
    """ A view to show about info about the page and organisation """

    template = 'info/info.html'

    return render(request, template)
