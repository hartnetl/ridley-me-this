from django.shortcuts import render
from .forms import ContactForm

def contact(request):
    """ A view to show contact page with contact form """
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)
