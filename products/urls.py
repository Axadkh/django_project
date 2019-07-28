from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='product'),
    path('new', views.new, name='newProducts'),


]