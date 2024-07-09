from django.contrib import admin
from .models import ContactModel, AppointmentModel, ListModel



@admin.register(ListModel)

@admin.register(AppointmentModel)

class AppointmentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']


@admin.register(ContactModel)

class ServiseModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'message']
    list_display_links = ['id', 'name', 'email', 'phone', 'message']
