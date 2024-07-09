from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import ServiseModel, DoctorsModel


class DoctorsView(TemplateView):
    template_name = 'main/doctors.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doctors'] = DoctorsModel.objects.all()
        return context





class ServiceView(TemplateView):
    template_name = 'main/service.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servises'] = ServiseModel.objects.all()
        return context

        # def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        # context['banners'] = BannerModel.objects.all()
        # return context

