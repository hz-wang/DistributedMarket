from django_cron import CronJobBase, Schedule
from django.core.files import File

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'services.my_cron_job'    # a unique code

    def do(self):
        f = open('/test.txt', 'a+')
        f.write('a\n')
        f.close()