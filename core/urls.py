from django.urls import path
from .views import IndexViwes

urlpatterns = [
    path('',IndexViwes.as_view(),name='index'),
]