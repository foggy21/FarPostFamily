from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import User as Profile

def catalog(request):
    users = User.objects.all()

    return render(request, 'users/catalog.html', {
        'users' : users
    })

@login_required
def profile(request):
    try:
        current_user = request.user
        profile_user = Profile.objects.filter(username=current_user)
    except Exception as e:
        profile_user = None
        print('Exception: ', e)
    return render(request, 'users/profile.html', {
        'profile' : profile_user
    })

