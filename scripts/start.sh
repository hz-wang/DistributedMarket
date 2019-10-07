#!/bin/bash

bin/spark-class org.apache.spark.deploy.master.Master -h master &
python3 /dmarket/manage.py runserver 0.0.0.0:8000
