from django.urls import path
from . import views

urlpatterns = [
    path('create/contact', views.create_contact, name='create-contact'),
    path('heba-kheer', views.heba_kheer, name='heba-kheer'),
    path('technical-support', views.add_technical, name='technical-support'),
    path('technical-list', views.technical_list, name='technical-list'),
    path('home-employee', views.home_employee, name='home-employee'),

]
