from django import forms
from .models import ContactModel, AppointmentModel


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = AppointmentModel
        exclude = ['created_at']
        widgets = {
            'name' : forms.TextInput(attrs={
                'placeholder' : 'Name',
                'class' : 'form-control border-0',
                'style' : 'height: 55px'
            }),
            'email' : forms.EmailInput(attrs={
                'placeholder' : 'Email',
                'class' : 'form-control border-0',
                'style' : 'height: 55px'
            }),
            'phone' : forms.TextInput(attrs={
                'placeholder' : 'Phone',
                'class' : 'form-control border-0',
                'style' : 'height: 55px'
            }),
            'date' : forms.DateInput(attrs={
                'placeholder' : 'Date',
                'class' : 'form-control border-0',
                'style' : 'height: 55px'
            }),
            'choose' : forms.TextInput(attrs={
                'placeholder' : 'Choose',
                'class' : 'form-control border-0',
                'style' : 'height: 55px',

            }),
            'time' : forms.TimeInput(attrs={
                'placeholder' : 'Time',
                'class' : 'form-control border-0',
                'style' : 'height: 55px'
            }),
            'problem' : forms.TextInput(attrs={
                'placeholder' : 'Problem',
                'class' : 'form-control border-0',
                'style' : 'height: 55px'

            })
           
            
        }



class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        exclude = ['created_at']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Name',
                # 'class': 'form-control',
                
            }), 
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email',
                # 'class': 'form-control',
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Phone',
                # 'class': 'form-control',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Message',
                # 'class': 'form-control',
            })
        }
