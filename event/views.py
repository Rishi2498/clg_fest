from .forms import *
from .models import *
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_protect
from django.core.mail import EmailMessage
from django.contrib import messages
# Create your views here.
def home(request):
    events = Event.objects.all().order_by('-created_at')
    categories = category.objects.all()
    return render(request, 'home.html', {'events': events, 'categories': categories})

def category_detail(request, category_id):
    cat = get_object_or_404(category, id=category_id)
    
    # Get events that belong to this category
    events = Event.objects.filter(category=cat)
    
    return render(request, 'category_detail.html', {'category': category, 'events': events})

def category_events(request, category_slug):
    # Fetch the category based on the slug
    category_instance = get_object_or_404(category, slug=category_slug)
    
    # Get all events related to this category
    events = Event.objects.filter(category=category_instance).order_by('-created_at')

    return render(request, 'category_events.html', {'category': category_instance, 'events': events})

def event_detail(request, event_slug):
    # Get the event based on its slug
    event_instance = get_object_or_404(Event, slug=event_slug)
    page_name = event_instance.title.replace(" ", "_").lower() 
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            # Save the contact data to the database
            contact_form.save()
            # Redirect to the same page with a success message or show a success message
            return redirect('event_detail', event_slug=event_slug)  # You can display a success message here
    
    else:
        contact_form = ContactForm()
    return render(request, 'event_detail.html', {'event': event_instance, 'contact_form': contact_form})
'''    
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()  # Save form data to database

            # Get selected events using 'title' instead of 'name'
            selected_events = ", ".join(contact.events.values_list('title', flat=True))

            # Construct the email message
            subject = "Thank you for registering!"
            message = f"""
            Dear {contact.name},

            Thank you for registering for the Tech-Trix 2k25.

            Your details:
            Name: {contact.name}
            Email: {contact.email}
            Phone: {contact.phone}
            College: {contact.clg_name}
            Branch: {contact.branch}
            Year: {contact.get_year_display()}

            Selected Events: {selected_events}

            Best regards,
            Event Team
            """

            # Send email
            email = EmailMessage(subject, message, to=[contact.email])
            try:
                email.send()
                messages.success(request, "Registration successful! A confirmation email has been sent.")
            except:
                messages.warning(request, "Registration saved, but email could not be sent.")

            return redirect('thank_you')  # Redirect to a success page (define in urls.py)
        else:
            messages.error(request, "Error in form submission. Please correct the fields below.")
    else:
        form = ContactForm()

    return render(request, "form.html", {"form": form})
'''
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()  # Save form data to the database
            
            # Get the selected events
            events_selected = ", ".join([event.title for event in contact.events.all()])
            
            # Send a thank-you email
            subject = "Thank You for Registering"
            message = f"""
            Dear {contact.name},
            Greetings from Samskruti College of Engineering and Technology .   

            Thank you for registering TECTRIX-2K25!

            You have successfully registered for the following events:
            {events_selected}

            We look forward to seeing you.
            This acknowledgement should be shown to registration committee on the day of the event for payment.

            Best Regards,
            Prof. J.Mohan
            Convener- TECTRIX 2K25
            """
            from_email = "techtrix2k25@gmail.com"   # Update with your email
            recipient_list = [contact.email]
            send_mail(subject, message, from_email, recipient_list)
            
            messages.success(request, "Thank you for registering! A confirmation email has been sent.")
            return redirect("thank_you")  # Redirect to a success page
    else:
        form = ContactForm()
    return render(request, "form.html", {"form": form})
    
def thank_you(request):
    return render(request, 'tq.html')
