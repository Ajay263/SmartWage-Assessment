from django.db import models

# Create your models here.

from django.db import models

class Whatsapp(models.Model):
    user = models.CharField(max_length= 20)
    message = models.CharField(max_length= 20)
  

