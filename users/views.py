from typing import Any, Dict
from django.shortcuts import render, reverse
from django.views.generic import TemplateView, CreateView
from .forms import ContactForm, AppointmentForm
from .models import ListModel, AppointmentModel
from django.http import HttpResponse
import datetime





class ContactView(TemplateView):
    template_name = 'main/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_form'] = ContactForm()
        return context
    

class ContactCreateView(CreateView):
    form_class = ContactForm

    def get_success_url(self):
        return reverse('users:contact')



class AppointmentView(TemplateView):
    template_name = 'main/appointment.html'
    
    

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['app_form'] = AppointmentForm()
        context['list_items'] = ListModel.objects.all()
        return context
    


    
    def post(self, request, *args, **kwargs):
        posted_data = request.POST
 
        name = posted_data.get('name')
        email = posted_data.get('email')
        phone = posted_data.get('phone')
        date = posted_data.get('date')

        try:
            date = datetime.datetime.strptime(date, "%m/%d/%Y")
            date = date.strftime("%Y-%m-%d")
        except ValueError:
            pass

        time = posted_data.get('time')

        try:
            time = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S') 
        except ValueError:
            pass

        doctors = posted_data.get('doctors')
        problem = posted_data.get('problem')  
        appointment = AppointmentModel(name=name, email=email, phone=phone, date=date, time=time, doctors=doctors, problem=problem)
        appointment.save()
        
        print(name, email, phone, date, time, doctors, problem)

        return HttpResponse('data saved successfully')
    





        

        
        

