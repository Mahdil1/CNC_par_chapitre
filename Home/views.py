from django.shortcuts import render
from .models import contact
from django.http import HttpResponse

# Create your views here.

def home(request):
    if request.method == 'POST':
        # Assuming you have data from a form submission
        nom = request.POST.get('name')
        mail = request.POST.get('email')
        mess = request.POST.get('message')

        # Create a new ConcourChimie object and save it to the database
        messages = contact(
            nom = nom,
            email = mail,
            message = mess
        )
        messages.save()

    return render(request, 'index.html')

