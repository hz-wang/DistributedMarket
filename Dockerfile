FROM gettyimages/spark

RUN apt-get update \
 && apt-get install -y mysql-server \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN pip3 install Django==2.1.*
