FROM hadoop-spark

RUN pip3 install Django==2.1.*
RUN pip3 install psycopg2-binary
RUN pip3 install django-cron