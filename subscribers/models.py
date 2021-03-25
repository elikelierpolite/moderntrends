from django.db import models

class Subscriber(models.Model):
  email = models.CharField(null=True, blank=True, max_length=200)