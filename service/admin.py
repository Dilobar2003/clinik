from django.contrib import admin
from .models import ServiseModel, DoctorsModel


@admin.register(ServiseModel)

class ServiseModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
   

@admin.register(DoctorsModel)

class BannerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'job']
    list_display_links = ['id', 'name', 'job']    