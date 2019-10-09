import subprocess
import threading
import os

class Spark:

    @staticmethod
    def jobExit(proc):
        print('Job Completed.')

    @staticmethod
    def submitJob():
        # subprocess.Popen(
        #     [
        #         os.environ['SPARK_HOME'] + '/bin/spark-submit',
        #         '--master', 'yarn',
        #         '--deploy-mode', 'cluster',
        #         '--queue', 'default',
        #         '--num-executors', '2',
        #         '--executor-memory', '2G',
        #         '--archives', '/sample/mnist/mnist.zip#mnist',
        #         '/sample/code/mnist_data_setup.py',
        #         '--output', 'mnist/csv',
        #         '--format', 'csv'
        #     ]
        # )
        print('submitJob')
        subprocess.Popen(
            [
                os.environ['SPARK_HOME'] + '/bin/spark-submit',
                '--master', 'yarn',
                '--deploy-mode', 'cluster',
                '--queue', 'default',
                '--num-executors', '2',
                '--executor-memory', '2G',
                '--py-files', '/sample/code/spark/mnist_dist.py',
                '--conf', 'spark.dynamicAllocation.enabled=false',
                '--conf', 'spark.yarn.maxAppAttempts=1',
                '--conf', 'spark.executorEnv.LD_LIBRARY_PATH=' + os.environ['LIB_JVM'] + ':' + os.environ['LIB_HDFS'],
                '--conf', 'spark.executorEnv.CLASSPATH=' + os.environ['CLASSPATH'],
                '--conf', 'spark.executorEnv.LIB_HDFS=' + os.environ['LIB_HDFS'],
                '--conf', 'spark.executorEnv.LIB_JVM=' + os.environ['LIB_JVM'],
                '--conf', 'spark.yarn.appMasterEnv.PYSPARK_PYTHON=' + os.environ['PYSPARK_PYTHON'],
                '--conf', 'spark.pyspark.python=' + os.environ['PYSPARK_PYTHON'],
                '--conf', 'spark.yarn.appMasterEnv.PYTHONPATH=' + os.environ['PYSPARK_PYTHON'],
                '--conf', 'spark.executorEnv.SPARK_YARN_USER_ENV=' + os.environ['SPARK_YARN_USER_ENV'],
                '/sample/code/spark/mnist_spark.py',
                '--images', 'mnist/csv/train/images',
                '--labels', 'mnist/csv/train/labels',
                '--mode', 'train',
                '--model', 'mnist_model'
            ]
        )

        return

        # def runInThread(onExit):
        #     proc = subprocess.Popen(
        #         [
        #             '/usr/spark-2.4.1/bin/spark-submit',
        #             '/usr/spark-2.4.1/examples/src/main/python/pi.py',
        #             '10' 
        #         ]
        #     )
        #     proc.wait()
        #     onExit(proc)
        #     return
        # thread = threading.Thread(target=runInThread,
        #                         args=(Spark.jobExit,))
        # thread.start()
        # return