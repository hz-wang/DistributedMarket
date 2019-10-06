from django.db import models
from django.template.loader import render_to_string
from django.contrib.auth.models import User
# Create your models here.

class Credit(models.Model):
    sharing_credit = models.IntegerField()
    using_credit = models.IntegerField()
    rate = models.FloatField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.id

class Profile(models.Model):
    # user_id, password, email_address in User
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default='', blank=False)
    credit = models.OneToOneField(Credit, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

class Machine(models.Model):
    machine_id = models.AutoField(primary_key=True)
    machine_type = models.CharField(max_length=40, default='GPU', blank=True)	
    ip_address = models.CharField(max_length=64, default='127.0.0.1', blank=True)	
    service_port = models.CharField(max_length=32, default='8000', blank=True)	
    core_num = models.IntegerField(default=1, blank=True)
    memory_size = models.FloatField(null=True)
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
        return 'job_id:{}, root_path:{}, core_num:{}, machine_type:{}, status:{}, user_id:{}'.format(self.job_id, self.root_path, self.core_num, self.machine_type, self.status, self.user.id)



# class Metadata(models.Model):
#     machine_info = models.ListCharField(
#         base_field = models.CharField(max_length=100),
#         size=100,
#     )

