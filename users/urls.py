from django.urls import path
from .views import AppointmentView, ContactView, ContactCreateView

app_name = 'users'
urlpatterns = [
    path('appointment/', AppointmentView.as_view(), name='appointment'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact/create/', ContactCreateView.as_view(), name='contact_create'),



]