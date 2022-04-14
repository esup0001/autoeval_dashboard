from unicodedata import name
from django.urls import path

from .views import dashboard, index, table


urlpatterns = [
    path('todos/', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('table/', table, name='table')
]