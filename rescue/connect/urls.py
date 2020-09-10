from django.urls import path
from .views import (index, center, show_needs, add_help_center, add_need)


app_name = 'connect'
urlpatterns = [
    path('', index, name='index'),
    path('list_help_needs/', show_needs, name='list_help'),
    path('add_help_center/', add_help_center, name='add_help_center'),
    path('add_need/', add_need, name='add_need'),
    path('<pk>/', center, name='center'),
]
