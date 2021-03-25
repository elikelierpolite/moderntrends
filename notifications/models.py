from django.db import models
from accounts.models import Account

class Notification(models.Model):
  title = models.CharField(max_length=200, null=True, blank=True)
  hook = models.CharField(max_length=200, null=True, blank=True)
  img = models.CharField(max_length=200, null=True, blank=True)
  cta = models.CharField(max_length=200, null=True, blank=True)
  url = models.CharField(max_length=200, null=True, blank=True)
  seen = models.BooleanField(default=False)
  to = models.ForeignKey(Account, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.title