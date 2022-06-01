from django.db import models

# Create your models here.

class Links(models.Model): 
  link = models.CharField(max_length=255, blank=False, null=False)
  shortened_link = models.CharField(max_length=5, unique=True)

  def __str__(self): 
    return self.shortened_link