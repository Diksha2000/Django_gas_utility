from django.db import models

# Create your models here.
from django.db import models
from consumer.models import Customer, ServiceRequest

class SupportAgent(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    # Add other fields as needed

class Inquiry(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    agent = models.ForeignKey(SupportAgent, on_delete=models.SET_NULL, null=True, blank=True)
    inquiry_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('open', 'Open'), ('resolved', 'Resolved')])
    subject = models.CharField(max_length=200)
    description = models.TextField()
    # Add other fields as needed

class Interaction(models.Model):
    inquiry = models.ForeignKey(Inquiry, on_delete=models.CASCADE)
    interaction_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    # Add other fields as needed

