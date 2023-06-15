from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('add-person/', views.add_person, name='add_person'),
]
