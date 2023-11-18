from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .forms import LoginForm
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('catalog/', views.catalog, name='users-catalog'),
    path('auth/', auth_views.LoginView.as_view(template_name='users/auth.html', authentication_form=LoginForm), name="login" )
]
