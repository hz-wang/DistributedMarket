${SPARK_HOME}/bin/spark-submit \
--master yarn \
--deploy-mode cluster \
--queue default \
--num-executors 2 \
--executor-memory 2G \
--py-files hdfs:///user/root/mnist/input/code/spark/mnist_dist.py \
--conf spark.dynamicAllocation.enabled=false \
--conf spark.yarn.maxAppAttempts=1 \
--conf spark.executorEnv.LD_LIBRARY_PATH=$LIB_JVM:$LIB_HDFS \
--conf spark.executorEnv.CLASSPATH=$(hadoop classpath --glob) \
hdfs:///user/root/mnist/input/code/spark/mnist_spark.py \
--images mnist/output/test/images \
--labels mnist/ouput/test/labels \
--mode inference \
--model mnist/output/mnist_model \
--output mnist/output/predictions
