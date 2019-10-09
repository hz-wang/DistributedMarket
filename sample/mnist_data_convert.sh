${SPARK_HOME}/bin/spark-submit \
--master yarn \
--deploy-mode cluster \
--queue default \
--num-executors 2 \
--executor-memory 2G \
--archives /sample/mnist/mnist.zip#mnist \
/sample/code/mnist_data_setup.py \
--output mnist/csv \
--format csv