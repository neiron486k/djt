from django.urls import path
from .views import PagesViewSet

app_name = 'pages'
urlpatterns = [
    path('', PagesViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>', PagesViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update'})),
]
