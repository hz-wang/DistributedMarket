#!/bin/bash

/etc/init.d/ssh start
stop-dfs.sh
start-dfs.sh
start-yarn.sh
python3 /dmarket/manage.py runserver 0.0.0.0:8000
