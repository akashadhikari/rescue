from django.urls import path
from .views import (index, center)


app_name = 'connect'
urlpatterns = [
    path('', index, name='index'),
    path('<pk>', center, name='center')
]
