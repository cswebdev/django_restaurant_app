from django.urls import path

from .views import MenuitemListAPIView  
urlpatterns = [
    path('', MenuitemListAPIView.as_view())
]
