import subprocess
import threading

class Spark:

    @staticmethod
    def jobExit(proc):
        print('Job Completed.')

    @staticmethod
    def submitJob():
        subprocess.Popen(
            [
                '/usr/spark-2.4.1/bin/spark-submit',
                '/usr/spark-2.4.1/examples/src/main/python/pi.py',
                '10'
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