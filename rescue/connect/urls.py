from django.urls import path
from .views import (index, center, show_needs, add_help_center, add_need, show_helps, add_help)


app_name = 'connect'
urlpatterns = [
    path('', index, name='index'),
    path('list_needs/', show_needs, name='list_need'),
    path('list_helps/', show_helps, name='list_help'),
    path('add_help_center/', add_help_center, name='add_help_center'),
    path('add_need/', add_need, name='add_need'),
    path('add_help/', add_help, name='add_help'),
    path('<pk>/', center, name='center'),
]
