from django.db import models
from django.template.loader import render_to_string
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    # user_id, password, email_address in User
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default='', blank=False)
    credit = models.OneToOneField(Credit)

    def __str__(self):
        return self.user

class Machine(models.Model):
    machine_id = models.AutoField(primary_key=True)
    machine_type = models.CharField(max_length=40, default='GPU', blank=True)	
    ip_address = models.CharField(max_length=64, default='127.0.0.1', blank=True)	
    service_port = models.CharField(max_length=32, default='8000', blank=True)	
    core_num = models.IntegerField(default=1, blank=True)
    memory_size = models.DoubleField(null=True)
    time_period = models.IntegerField(null=True)
    available = models.BooleanField(default=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.machine_id

class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    root_path = models.CharField(max_length=128, default='', blank=True)
    core_num = models.IntegerField()
    machine_type = models.CharField(max_length=40, default='GPU', blank=True)
	status = models.CharField(max_length=40, default='Available', blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
        return self.job_id

class Credit(models.Model):
	sharing_credit = models.IntegerField()
	using_credit = models.IntegerField()
	rate = models.DoubleField(null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):	
        return self.user.id

class Metadata(models.Model):
	machine_info = ListCharField(
        base_field=CharField(max_length=100),
        size=100,
    )

