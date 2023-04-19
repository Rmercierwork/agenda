from django.urls import path
from . import views

app_name = 'my_agenda'

urlpatterns = [
    path('', views.agenda_list, name='agenda_list'),
    path('contacts/', views.contact_list, name='contact_list'),
    path('add/', views.add_contact, name='add_contact'),
    path('update/<int:pk>/', views.update_contact, name='update_contact'),
    path('delete/<int:pk>/', views.delete_contact, name='delete_contact'),
    path('add_agenda/', views.add_agenda, name='add_agenda'),
    path('delete_agenda/<int:pk>/', views.delete_agenda, name='delete_agenda'),
]
