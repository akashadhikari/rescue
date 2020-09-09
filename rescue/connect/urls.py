from django.urls import path
from .views import (index)


app_name = 'connect'
urlpatterns = [
    path('', index, name='index'),
]
