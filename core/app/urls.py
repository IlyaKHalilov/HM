from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', main_render, name='main'),
    path('product/<int:pk>/', detail_render, name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
