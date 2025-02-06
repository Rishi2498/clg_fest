from django.db import models
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(unique=True, default='default-slug')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)
    def __str__(self):
        return self.name
    
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(category, on_delete=models.SET_DEFAULT, default=1) 
    slug = models.SlugField(unique=True, default='default-slug')
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)

    def save(self, *args, **kwargs):
        # Auto-generate slug from title if it's empty
        if not self.slug:
            self.slug = slugify(self.title)
        
        # Ensure the slug is unique
        original_slug = self.slug
        counter = 1
        while Event.objects.filter(slug=self.slug).exists():
            self.slug = f"{original_slug}-{counter}"
            counter += 1

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    clg_name = models.CharField(max_length=500)
    branch = models.CharField(max_length=500)
    pin = models.CharField(max_length=60)
    YEAR_CHOICES = [
    ('1', '1st Year'),
    ('2', '2nd Year'),
    ('3', '3rd Year'),
]
    year = models.CharField(max_length=1, choices=YEAR_CHOICES)
    events = models.ManyToManyField('Event',)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when record is created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically set when record is updated

    def __str__(self):
        return self.name