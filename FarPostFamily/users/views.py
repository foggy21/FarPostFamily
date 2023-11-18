from django.shortcuts import render
from .models import User

def catalog(request):
    users = User.objects.all()

    return render(request, 'users/catalog.html', {
        'users' : users
    })

