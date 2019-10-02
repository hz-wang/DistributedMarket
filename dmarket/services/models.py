from django.db import models
from django.template.loader import render_to_string
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
	# user_id, password, email_address in User
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default='', blank=True)
    credit = models.OneToOneField(Credit)
    followers = models.ManyToManyField(User, related_name='self', blank=True)

    def __str__(self):
        return self.user

class Machine(models.Model):
	machine_id = 



class Job(models.Model):


class Metadata(models.Model):


class Credit(models.Model):
	sharing_credit = 