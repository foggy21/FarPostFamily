from django.urls import path
from .views import UserListCreate, UserRetriveUpdateDelete

urlpatterns = [
    path('', UserListCreate.as_view(), name='user-create'),
    path('user/<int:pk>', UserRetriveUpdateDelete.as_view(), name='user-detail')
]