from rest_framework import generics

from .models import Menuitem
from .serializers import MenuSerializer


# Create your views here.
class MenuitemListAPIView(generics.ListAPIView):
    queryset = Menuitem.objects.all()
    serializer_class = MenuSerializer