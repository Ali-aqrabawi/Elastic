from django.db import models



from djangae import fields, storage
from djangae.db import transaction
# Create your models here.

class Contactus(models.Model):
    name = models.CharField(max_length=250, null=True)
    email = models.CharField(max_length=250, null=True)
    subject = models.CharField(max_length=250, null=True)
    message = models.CharField(max_length=250, null=True)