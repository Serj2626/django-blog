from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('contacts/', views.contacts, name='blog-contacts'),
]
