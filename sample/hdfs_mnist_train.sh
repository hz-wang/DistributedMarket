/usr/local/spark/bin/spark-submit \
--master yarn \
--deploy-mode cluster \
--queue default \
--num-executors 2 \
--executor-memory 2G \
--py-files hdfs:///user/root/mnist/input/code/spark/mnist_dist.py \
--conf spark.dynamicAllocation.enabled=false \
--conf spark.yarn.maxAppAttempts=1 \
hdfs:///user/root/mnist/input/code/spark/mnist_spark.py \
--images mnist/output/train/images \
--labels mnist/output/train/labels \
--mode train \
--model mnist/output/mnist_model
