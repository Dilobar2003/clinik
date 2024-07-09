from django.urls import path
from .views import ServiceView, DoctorsView

app_name = 'servise'
urlpatterns = [
    path('service/', ServiceView.as_view(), name='service'),
    path('doctors/', DoctorsView.as_view(), name='doctors')


]