from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import BannerModel






class HomeView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banners'] = BannerModel.objects.all()
        return context


class CommentView(TemplateView):
    template_name = 'main/testimonial.html'    


class AboutView(TemplateView):
    template_name = 'main/about.html'