from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import UserListCreate, UserRetriveUpdateDelete

urlpatterns = [
    path('', UserListCreate.as_view(), name='user-create'),
    path('<int:pk>/', UserRetriveUpdateDelete.as_view(), name='user-detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   
