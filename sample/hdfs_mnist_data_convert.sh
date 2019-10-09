${SPARK_HOME}/bin/spark-submit \
--master yarn \
--deploy-mode cluster \
--queue default \
--num-executors 2 \
--executor-memory 2G \
--archives hdfs:///user/root/mnist/input/data/mnist.zip#mnist \
hdfs:///user/root/mnist/input/code/mnist_data_setup.py \
--output mnist/output \
--format csv
