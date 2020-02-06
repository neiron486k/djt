from rest_framework import viewsets
from .models import Pages
from .serializers import PageSerializer


class PagesViewSet(viewsets.ModelViewSet):
    queryset = Pages.objects.all()
    serializer_class = PageSerializer
