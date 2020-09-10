from django.urls import path
from .views import (index, center, show_needs, add_help_center)


app_name = 'connect'
urlpatterns = [
    path('', index, name='index'),
    path('need_help/', show_needs, name='need_help'),
    path('add_help_center/', add_help_center, name='add_help_center'),
    path('<pk>/', center, name='center'),
]
