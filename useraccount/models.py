from django.db import models
from django.contrib.auth.models import User
from django.core.validators import EmailValidator, MinLengthValidator, MaxLengthValidator

# Create your models here.
class Profile(models.Model):
    
    GENDER_OPT = (
        (('male'), ('Male')),
        (('female'), ('Female')),
        (('other'), ('Other')),
        ('', '')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    phone = models.PositiveIntegerField()
    email = models.EmailField(max_length=50,validators=[
        EmailValidator(), MinLengthValidator(10)])
    gender = models.CharField(blank=True, max_length=10, choices=GENDER_OPT)
    date_created = models.DateTimeField(auto_now_add=True)
    
