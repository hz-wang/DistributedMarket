from django_cron import CronJobBase, Schedule
from django.core.files import File
from .spark.spark import *
from .models import *

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'services.my_cron_job'    # a unique code

    def do(self):
        print('cron run')
        newJobs = Job.objects.filter(status='new')
        if len(newJobs) == 0:
            print('no new jobs')
            return
        print('has new job')
        oneJob = newJobs.first()
        oneJob.status = 'running'
        oneJob.save()
        Spark.submitJob()
        return
