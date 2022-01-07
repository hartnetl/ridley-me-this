from django.shortcuts import render


def contact(request):
    """ A view to show contact page with contact form """

    return render(request, 'contact/contact.html')
