
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('category/<slug:category_slug>/', views.category_events, name='category_events'),  # Event list by category
    path('event/<slug:event_slug>/', views.event_detail, name='event_detail'),
    path('contact/', views.contact_view, name='contact'),
    path('thank-you/', views.thank_you, name='thank_you'), 
]
