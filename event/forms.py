from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    
    class Meta:

        model = Contact
        fields = ['name', 'email', 'phone', 'clg_name', 'branch', 'pin', 'year', 'events']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'clg_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'College Name'}),
            'branch': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Branch'}),
            'pin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Roll no.'}),
            'year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Year(1,2,3)'}),
            'events': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
        }
       
    # Optionally add custom validation or custom widgets if needed
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Add custom validation for the email (e.g., check if it's unique)
        if Contact.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        # Add custom validation for phone number format if needed (e.g., valid phone number format)
        if phone and len(phone) < 10:
            raise forms.ValidationError("Phone number must be at least 10 digits.")
        return phone
    
    def clean_year(self):
        year = self.cleaned_data.get('year')
        # Add custom validation for the year, if needed
        if year and not year.isdigit():
            raise forms.ValidationError("Year must be a valid number.")
        return year

