from django.db import models
# Create your models here.

class Reviews(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=500)
    message = models.TextField()